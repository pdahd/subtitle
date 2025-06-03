## English Instructions

Hello, Jules. I have an SRT file [input_filename.srt]. I want you to perform the following operations:

1. Examine this SRT file.
2. For each subtitle block in the file:
    - Keep its original sequence number and timeline.
    - Replace its original English dialogue text with the following placeholder format: 需要人工翻译：【<Original English Text>】请在此处填写翻译。 (where <Original English Text> is the original English dialogue content of that block.)
3. Ensure that the final output SRT file format is correct (sequence number, timeline, newly generated placeholder text, blank lines between blocks).
4. Save the processed result as a new SRT file named [output_filename.srt].

---

## 中文说明

你好，Jules。我有一个SRT文件，文件名是 输入文件名.srt。我希望你帮我处理一下：

1. 首先，请查阅这个 输入文件名.srt 文件的内容。
2. 然后，对于文件里的每一个字幕块，请进行如下操作：
    - 这个字幕块原来的序号和时间轴信息需要完整保留。
    - 这个字幕块原来的英文对白文本，请用下面这种格式的新文本来替换掉： 需要人工翻译：【这里是该块的原始英文对白】请在此处填写翻译。 （请注意，上面格式里的 【这里是该块的原始英文对白】 部分，需要替换成这个字幕块实际的、原始的英文对白内容。）
3. 最后，请确保整个文件是标准SRT格式，也就是说，每个块都有序号、时间轴、替换后的新文本，并且块和块之间有一个空行隔开。
4. 请将这样处理完成的所有内容，保存到一个新的SRT文件里，文件名叫做 输出文件名.srt。
