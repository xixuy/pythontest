"""
    作者：西西
    版本：1.0
    日期：2019/06/24
    功能：判断密码强弱
"""

def check_num_exist(password_str):
    """
    判断字符串中是否含有数字
    :param password_str:
    :return:
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    """
    判断字符串中是否含有字母
    :param password_str:
    :return:
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    """
    主函数
    :return:
    """
    password=input('请输入密码：')

    strength_level=0

    #规则一：判断密码长度
    if len(password)>=8:
        strength_level+=1
    else:
        print('面命长度至少要求8位！')

    #规则二：包含数字
    if check_num_exist(password):
        strength_level+=1
    else:
        print('密码要求包含数字!')

    # 规则三：包含字母
    if check_letter_exist(password):
        strength_level += 1
    else:
        print('密码要求包含字母!')

    if strength_level==3:
        print('恭喜！密码强度合格！')
    else:
        print('密码强度不合格!')


if __name__ == '__main__':
    main()