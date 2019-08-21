"""
    作者：西西
    版本：3.0
    日期：2019/06/26
    功能：模拟掷筛子
    2.0增加功能：模拟投掷两个筛子
    3.0增加功能：可视化模拟投掷两个筛子的结果
    知识点：matplotlib模块
"""

import random
import matplotlib.pyplot as plt


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
    total_times=100
    #初始化次数列表
    result_list=[0]*11

    #初始化点数列表
    roll_list=list(range(2,13))

    roll_dict=dict(zip(roll_list,result_list))

    #记录
    roll1_list=[]
    roll2_list=[]

    for i in range(total_times):
        roll1=roll_dice()
        roll2=roll_dice()
        #把每次的点数记录到列表中
        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2,13):
            if (roll1+roll2)==j:
                roll_dict[j]+=1
    #遍历字典
    for i,result in roll_dict.items():

        print('点数{}的次数：{}，频率{}'.format(i,result,result/total_times))

    #数据可视化
    x=range(1,total_times+1)
    plt.scatter(x,roll1_list,alpha=0.5,c='red')
    plt.scatter(x, roll2_list,alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()