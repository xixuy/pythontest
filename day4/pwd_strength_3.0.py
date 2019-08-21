"""
    作者：西西
    版本：3.0
    日期：2019/06/24
    功能：判断密码强弱
    增加功能：保存密码及强度到文件中
"""

def check_num_exist(password_str):
    """
    判断字符串中是否含有数字
    :param password_str:
    :return:
    """
    has_number=False
    for c in password_str:
        if c.isdigit():
            has_number=True
            break
    return has_number


def check_letter_exist(password_str):
    """
    判断字符串中是否含有字母
    :param password_str:
    :return:
    """
    has_letter=False
    for c in password_str:
        if c.isalpha():
            has_letter=True
            break
    return has_letter


def main():
    """
    主函数
    :return:
    """

    try_times=5

    while try_times>0:

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

        # 将密码保存到文件中
        f = open('password_3.0.txt', 'a')
        f.write('密码是{}，强度是{}\n'.format(password,strength_level))
        f.close()

        if strength_level==3:
            print('恭喜！密码强度合格！')

            break
        else:
            print('密码强度不合格!')
            try_times-=1



    if try_times<=0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()