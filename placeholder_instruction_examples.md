# 指令示例：为SRT文件添加占位符

## 英文指令示例

Hello Jules. I have an SRT file `[Input Filename.srt]`. I'd like you to perform the following actions:

1.  **Read** the content of this `[Input Filename.srt]` file.
2.  For **each subtitle block** in the file:
    *   Its original **sequence number** and **timestamp** must be fully preserved.
    *   Its original **English dialogue text** should be replaced with a new text in the following format:
        `NEEDS MANUAL TRANSLATION: [<Original English Text>] Please fill in the translation here.`
        (Note: The `<Original English Text>` part in the format above should be replaced with the actual original English dialogue content of that block.)
3.  Ensure the final output SRT file is correctly formatted (sequence number, timestamp, the newly generated placeholder text, and a blank line energijeach block).
4.  Save all processed content into a **new SRT file** named `[Output Filename.srt]`.

## 中文指令示例

你好，Jules。我有一个SRT文件，文件名是 `输入文件名.srt`。我希望你帮我处理一下：

1.  首先，请**读取**这个 `输入文件名.srt` 文件的内容。
2.  然后，对于文件里的**每一个字幕块**，请进行如下操作：
    *   这个字幕块原来的**序号**和**时间轴**信息需要完整保留。
    *   这个字幕块原来的**英文对白文本**，请用下面这种格式的**新文本**来**替换**掉：
        `需要人工翻译：【这里是该块的原始英文对白】请在此处填写翻译。`
        （请注意，上面格式里的 `【这里是该块的原始英文对白】` 部分，需要替换成这个字幕块实际的、原始的英文对白内容。）
3.  最后，请确保整个文件是标准SRT格式，也就是说，每个块都有序号、时间轴、替换后的新文本，并且块和块之间有一个空行隔开。
4.  请将这样处理完成的所有内容，保存到一个**新的SRT文件**里，文件名叫做 `输出文件名.srt`。
