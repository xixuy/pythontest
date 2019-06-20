"""
    功能：BMR计算器
    版本：1.0
    日期：2019/06/19
"""


def main():
    """
    主函数
    :return:
    """
    gender='男'

    weight=70

    height=175

    age=25
    if gender=='男':
        #男性
        bmr=13.7*weight+5.0*height-6.8*age+66
    elif gender=='女':
        #女性
        bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 65
    else:
        bmr=-1
    print(bmr)


if __name__ == '__main__':
    main()
