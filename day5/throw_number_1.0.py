"""
    作者：西西
    版本：1.0
    日期：2019/06/25
    功能：模拟掷骰子
    知识点：随机函数range()的用法,enumerate()函数同时可获取组合的索引和值
"""

import random


def roll_dice():
    """
    模拟掷筛子
    :return:
    """
    roll=random.randint(1,6) #生成随机数
    return roll


def main():
    """
    主函数
    :return:
    """
    #总的模拟次数
    total_times=1000
    #初始化列表[0,0,0,0,0,0]
    result_list=[0]*6

    for i in range(total_times):
        roll=roll_dice()
        for j in range(1,7):
            if roll==j:
                result_list[j-1]+=1 #列表相应的位置加1

    #遍历列表
    for i,result in enumerate(result_list):

        print('点数{}的次数：{}，频率{}'.format(i+1,result,result/total_times))


if __name__ == '__main__':
    main()