"""
    作者：xixi
    功能：绘制五角星
    版本：1.0
    日期：2019/06/18
"""
import turtle


def main():
    """
    主函数
    :return:
    """
    count=1

    while count<=5:
        # 向前走50像素
        turtle.forward(100)
        # 向右转144度角
        turtle.right(144)
        count+=1

    turtle.exitonclick()


if __name__=='__main__':
    main()