"""
    作者：xixi
    功能：绘制五角星
    版本：2.0
    日期：2019/06/18
"""
import turtle

#把绘制五角星的部分抽象为函数
def draw_pentagram(size):
    """
    绘制五角星
    :param size:
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

def main():
    """
    主函数
    :return:
    """

    size=50
    #使用循环绘制不同大小的五角星
    while size<=200:
        draw_pentagram(size)
        size+=10

    turtle.exitonclick()


if __name__=='__main__':
    main()