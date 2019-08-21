"""
    作者：西西
    版本：4.0
    日期：2019/06/26
    功能：模拟掷筛子
    2.0增加功能：模拟投掷两个筛子
    3.0增加功能：可视化模拟投掷两个筛子的结果
    4.0增加功能：直方图显示
    知识点：matplotlib模块
"""

import random
import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

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

    #记录
    roll_list=[]

    for i in range(total_times):
        roll1=roll_dice()
        roll2=roll_dice()
        roll_list.append(roll1+roll2)

    #数据可视化

    plt.hist(roll_list,bins=range(2,14),normed=1,edgecolor='black',linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')

    plt.show()


if __name__ == '__main__':
    main()