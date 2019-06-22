"""
    作者：西西
    功能：52周存钱挑战
    版本：4.0
    日期：2019/06/21
    增加功能：灵活设置每周的存款数
    知识点：全局变量与局部变量，函数
"""

import math

saving = 0  # 帐户累计

def save_money(money_per_week,increase_money,total_week):
    """
    计算n周内的存钱数
    :param money_per_week:
    :param increase_money:
    :param total_week:
    :return:
    """
    global saving
    money_list = []  # 记录每周存款数的列表
    # 使用循环直接计数
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)  # 对列表中的数据求和  #
        print("第{}周存入{}元，帐户累计{}元".format(i + 1, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_money
    return saving


def main():
    """
    主函数
    :return:
    """
    money_per_week=float(input('请输入每周存入的金额：'))   #每周存入的金额
    increase_money=float(input('请输入每周的递增金额：'))  #递增的金额
    total_week=int(input("请输入存钱的周数："))     #总共的周数

    save_money(money_per_week,increase_money,total_week)
    print("总的存款金额为：",saving)


if __name__ == '__main__':
    main()