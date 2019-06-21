"""
    作者：西西
    功能：52周存钱挑战
    版本：3.0
    日期：2019/06/21
    增加功能：使用循环直接计数
    知识点：for循环,range()从0开始计数
"""

import math


def main():
    """
    主函数
    :return:
    """
    money_per_week=10    #每周存入的金额
    increase_money=10   #递增的金额
    total_week=52     #总共的周数
    saving=0      #帐户累计

    money_list=[]   #记录每周存款数的列表

    #使用循环直接计数
    for i in range(total_week):
        money_list.append(money_per_week)
        saving=math.fsum(money_list)   #对列表中的数据求和  #
        print("第{}周存入{}元，帐户累计{}元".format(i+1,money_per_week,saving))
        # 更新下一周的存钱金额
        money_per_week+=increase_money


if __name__ == '__main__':
    main()