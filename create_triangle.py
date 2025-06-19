from PIL import Image, ImageDraw

# 定义图像尺寸
W, H = 200, 200

# 创建一个新的 RGBA 图像 (带透明通道)，背景透明
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# 获取 ImageDraw 对象
draw = ImageDraw.Draw(img)

# 定义三角形的顶点坐标
triangle_points = [
    (W / 2, H * 0.1),      # 顶点 (顶端中央)
    (W * 0.1, H * 0.9),    # 左下角顶点
    (W * 0.9, H * 0.9)     # 右下角顶点
]

# 定义填充颜色 (红色，RGBA格式)
red_color = (255, 0, 0, 255)

# 绘制填充的三角形
draw.polygon(triangle_points, fill=red_color)

# 定义输出文件名
filename = "red_triangle.png"

# 保存图像为PNG文件
try:
    img.save(filename)
    print(f"图片 '{filename}' 已成功创建。")
except Exception as e:
    print(f"保存图片时出错: {e}")
