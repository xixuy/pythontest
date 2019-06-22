"""
    作者：西西
    功能：52周存钱挑战
    版本：5.0
    日期：2019/06/21
    增加功能：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
    知识点：日期格式，datetime库
"""

import math
import datetime
saving = 0  # 帐户累计

def save_money(money_per_week,increase_money,total_week):
    """
    计算n周内的存钱数
    :param money_per_week:每周存入的金额
    :param increase_money:每周增加的金额
    :param total_week:总周数
    :return:每周的帐户累计
    """
    global saving
    money_list = []  # 记录每周存款数的列表
    saved_money_list=[]   #记录每周的帐户累计
    # 使用循环直接计数
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)  # 对列表中的数据求和
        saved_money_list.append(saving)

        # print("第{}周存入{}元，帐户累计{}元".format(i + 1, money_per_week, saving))
        # 更新下一周的存钱金额
        money_per_week += increase_money
    return saved_money_list


def main():
    """
    主函数
    :return:
    """
    money_per_week=float(input('请输入每周存入的金额：'))   #每周存入的金额
    increase_money=float(input('请输入每周的递增金额：'))  #递增的金额
    total_week=int(input("请输入存钱的周数："))     #总共的周数
    #调用函数
    saved_money_list = save_money(money_per_week,increase_money,total_week)

    #输入的日期对应的周应该小于总周数
    input_date_str=input('请输入日期(yyyy/mm/dd):')
    input_date=datetime.datetime.strptime(input_date_str,'%Y/%m/%d')
    #获取当前周数
    week_num=input_date.isocalendar()[1]
    print(week_num)
    # print("总的存款金额为：",saving)
    print('第{}周的存款：{}元'.format(week_num,saved_money_list[week_num -1]))


if __name__ == '__main__':
    main()