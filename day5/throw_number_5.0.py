"""
    作者：西西
    版本：4.0
    日期：2019/06/26
    功能：模拟掷筛子
    2.0增加功能：模拟投掷两个筛子
    3.0增加功能：可视化模拟投掷两个筛子的结果
    4.0增加功能：直方图绘制可视化
    5.0增加模块：科学计算
    知识点：numpy模块
"""

import random
import matplotlib.pyplot as plt
import numpy
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


def main():
    """
    主函数
    :return:
    """
    total_times=10000
    roll_arr1=numpy.random.randint(1,7,total_times)
    roll_arr2 = numpy.random.randint(1, 7, total_times)
    result_arr=roll_arr1+roll_arr2

    hist,bins=numpy.histogram(result_arr,bins=range(2,14))
    print(hist)
    print(bins)
    #数据可视化直方图
    tick_labels=['2点','3点','4点','5点', '6点', '7点', '8点', '9点','10点','11点','12点']
    tick_pops=numpy.arange(2,13)+0.5
    plt.xticks(tick_pops,tick_labels)
    plt.hist(result_arr,bins=range(2,14),density=1,edgecolor='black',linewidth=1,rwidth=0.8)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')

    plt.show()


if __name__ == '__main__':
    main()