"""
    作者：xixi
    功能：绘制分形树
    版本：1.0
    日期：2019/06/19

"""
import turtle


def draw_branch(branch_length):
    """
    绘制分形树
    :return:
    """
    if branch_length>5:
        #绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length-15)

        #绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length-15)

        #返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    """
    主函数
    :return:
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(80)
    turtle.pendown()
    draw_branch(100)
    turtle.exitonclick()


if __name__=='__main__':
    main()