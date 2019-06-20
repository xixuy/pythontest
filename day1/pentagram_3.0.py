"""
    作者：xixi
    功能：绘制五角星
    版本：3.0
    日期：2019/06/19
    新增功能：使用迭代函数绘制五角星
"""
import turtle

#递归函数
def draw_recursive(size):
    """
    迭代绘制五角星
    :return:
    """
    count = 1
    # 绘制五角星
    while count <= 5:
        # 向前走50像素
        turtle.forward(size)
        # 向右转144度角
        turtle.right(144)
        count += 1
    size+=10
    #设置终止条件
    if size<=200:
        draw_recursive(size)


def main():
    """
    主函数
    :return:
    """
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()
    turtle.pensize()
    size=50
    draw_recursive(size)
    turtle.exitonclick()


if __name__=='__main__':
    main()