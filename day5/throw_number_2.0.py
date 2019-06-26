"""
    作者：西西
    版本：2.0
    日期：2019/06/26
    功能：模拟投掷筛子
    2.0增加功能：模拟投掷两个筛子
    知识点：zip()函数，将两个列表打包为元组
"""

import random


def roll_dice():
    """
    模拟掷筛子
    :return:
    """
    roll=random.randint(1,6)
    return roll


def main():
    """
    主函数
    :return:
    """
    total_times=10000
    #初始化次数列表
    result_list=[0]*11

    #初始化点数列表
    roll_list=list(range(2,13))

    roll_dict=dict(zip(roll_list,result_list))

    for i in range(total_times):
        roll1=roll_dice() #第一个骰子的点数
        roll2=roll_dice() #第二个骰子的点数

        for j in range(2,13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1

    #遍历字典
    for i,result in roll_dict.items():

        print('点数{}的次数：{}，频率{}'.format(i,result,result/total_times))


if __name__ == '__main__':
    main()