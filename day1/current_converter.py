"""
   作者：
   功能：
   版本：
"""


def convert_currency(im,er):
    """
    汇率兑换功能
    :param im:
    :param er:
    :return:
    """
    out=im*er
    return out


def main():
    """
    主函数
    :return:
    """
    #汇率
    USD_VS_RMB=6.77

    #输入的金额
    currency_str_value=input('请输入待单位的金额：')
    unit=currency_str_value[-1]
    if unit=='￥':
        exchange_rate=1/USD_VS_RMB
    elif unit=='$':
        exchange_rate=USD_VS_RMB
    else:
        exchange_rate=-1

    if exchange_rate!=-1:
        money=eval(currency_str_value[:-1])
        out_money=convert_currency(money,exchange_rate)
        print('转换后的金额为：',out_money)
    else:
        print("不支持的货币")


if __name__=='__main__':
    main()

