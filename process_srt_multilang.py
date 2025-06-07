import argparse
import sys

def parse_srt_block(lines):
    """Parses a single SRT block."""
    if not lines:
        return None

    try:
        sequence = int(lines[0])
        timeline = lines[1]
        text = "\n".join(lines[2:])
        return {"sequence": sequence, "timeline": timeline, "text": text}
    except (IndexError, ValueError) as e:
        # print(f"Warning: Skipping invalid block: {lines} due to {e}", file=sys.stderr)
        return None

def srt_file_to_blocks(srt_content):
    """Parses SRT file content into a list of subtitle blocks."""
    blocks = []
    current_lines = []
    for line in srt_content.splitlines():
        line = line.strip()
        if line:
            current_lines.append(line)
        else:
            if current_lines:
                block = parse_srt_block(current_lines)
                if block:
                    blocks.append(block)
                current_lines = []

    if current_lines: # Add the last block if the file doesn't end with a blank line
        block = parse_srt_block(current_lines)
        if block:
            blocks.append(block)

    return blocks

def blocks_to_srt_string(blocks):
    """Converts a list of subtitle blocks back to SRT string format."""
    srt_string_parts = []
    for block in blocks:
        srt_string_parts.append(str(block["sequence"]))
        srt_string_parts.append(block["timeline"])
        srt_string_parts.append(block["text"])
        srt_string_parts.append("")  # Blank line separator
    return "\n".join(srt_string_parts)

def create_placeholder_text(original_text):
    """Creates the placeholder text with the original text embedded."""
    normalized_original_text = original_text.replace('\r\n', '\n')
    return f"---BLOCK_START---TRANSLATE_TEXT_BELOW:【{normalized_original_text}】END_OF_TEXT_TO_TRANSLATE. REPLACE_THIS_WHOLE_BLOCK_WITH_TRANSLATION---BLOCK_END---"

def create_placeholder_text_chinese(original_text):
    """Creates the Chinese placeholder text with the original text embedded."""
    normalized_original_text = original_text.replace('\r\n', '\n')
    return f"---区块开始---待翻译文本:【{normalized_original_text}】翻译完请替换整个区块---区块结束---"

def main():
    parser = argparse.ArgumentParser(description="Process SRT files to create translation placeholders.")
    parser.add_argument("--input", required=True, help="Path to the input SRT file.")
    parser.add_argument("--output", required=True, help="Path to the output processed SRT file.")
    parser.add_argument("--lang", default="en", choices=["en", "cn"], help="Language for placeholder text (en for English, cn for Chinese). Default is en.")

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            srt_content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file {args.input}: {e}", file=sys.stderr)
        sys.exit(1)

    subtitle_blocks = srt_file_to_blocks(srt_content)

    if not subtitle_blocks:
        print(f"Warning: No valid subtitle blocks found in {args.input}. Output file will be empty or may not be created as expected.", file=sys.stderr)
        processed_blocks = []
    else:
        processed_blocks = []
        for block in subtitle_blocks:
            if block and "text" in block:
                if args.lang == "cn":
                    placeholder = create_placeholder_text_chinese(block["text"])
                else:
                    placeholder = create_placeholder_text(block["text"])
                processed_blocks.append({
                    "sequence": block["sequence"],
                    "timeline": block["timeline"],
                    "text": placeholder
                })

    output_srt_string = blocks_to_srt_string(processed_blocks)

    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_srt_string)
        print(f"Successfully processed '{args.input}' and saved to '{args.output}'")
    except Exception as e:
        print(f"Error writing output file {args.output}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
