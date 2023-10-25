import turtle

# 创建Turtle对象
pen = turtle.Turtle()

# 设置边长（毫米）
side_length_mm = 50

# 假设屏幕DPI（像素密度）为 96，根据实际情况进行调整
dpi = 96

# 计算边长对应的像素长度
side_length_px = side_length_mm / 25.4 * dpi

# 将Turtle移动到起始位置
pen.penup()
pen.goto(-side_length_px / 2, 0)  # 将起点移到中心位置
pen.pendown()

# 绘制八边形
for _ in range(8):
    pen.forward(side_length_px)  # 向前移动边长的距离
    pen.right(45)  # 右转45度

# 关闭Turtle图形窗口
turtle.done()
