import zipfile
import os

# 定义要压缩的图片文件名
image_filename = "red_triangle.png"

# 定义输出的ZIP文件名
zip_filename = "red_triangle_archive.zip"

# 确保要压缩的文件存在
if not os.path.exists(image_filename):
    print(f"错误: 文件 '{image_filename}' 未找到。无法创建ZIP文件。")
else:
    try:
        # 创建一个新的ZIP文件，模式为写入 ('w')
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
            # 将图片文件添加到ZIP文件中
            zf.write(image_filename, os.path.basename(image_filename))

        print(f"文件 '{image_filename}' 已成功打包到 '{zip_filename}'。")

    except FileNotFoundError:
        print(f"错误: 源文件 '{image_filename}' 在压缩过程中未找到。")
    except Exception as e:
        print(f"创建ZIP文件时发生错误: {e}")
