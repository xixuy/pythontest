"""
    作者：西西
    功能：52周存钱挑战
    版本：1.0
    日期：2019/06/20
"""
def main():
    """
    主函数
    :return:
    """
    money_per_week=10    #每周存入的金额
    i=1
    increase_money=10   #递增的金额
    total_week=52     #总共的周数
    saving=0      #帐户累计

    while i<=total_week:
        #存钱操作
        saving+=money_per_week
        print("第{}周存入{}元，帐户累计{}元".format(i,money_per_week,saving))
        # 更新下一周的存钱金额
        money_per_week+=increase_money
        i+=1


if __name__ == '__main__':
    main()