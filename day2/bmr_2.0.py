"""
    功能：BMR计算器
    版本：2.0
    日期：2019/06/20
    增加功能：根据用户输入计算BMR值，程序持续运行
"""


def main():
    """
    主函数
    :return:
    """
    y_or_n=input('是否退出程序(y/n)?')

    while y_or_n!='y':

        gender=input('性别：')

        weight=float(input('体重(kg):'))

        height=float(input('身高(cm)：'))

        age=int(input('年龄：'))
        if gender=='男':
            #男性
            bmr=13.7*weight+5.0*height-6.8*age+66
        elif gender=='女':
            #女性
            bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 65
        else:
            bmr=-1
        print('基础代谢率：',bmr)



if __name__ == '__main__':
    main()
