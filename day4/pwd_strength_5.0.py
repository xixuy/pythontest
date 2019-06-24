"""
    作者：西西
    版本：5.0
    日期：2019/06/24
    功能：判断密码强弱
    增加功能：定义一个password工具类
"""

class PasswordTool:
    """
    密码工具类
    """
    def __init__(self,password):
        self.password=password
        self.strength_level=0

    def process_password(self):
        # 规则一：判断密码长度
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('面命长度至少要求8位！')

        # 规则二：包含数字
        if self.check_num_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字!')

        # 规则三：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母!')

    def check_num_exist(self):
        """
        判断字符串中是否含有数字
        :param password_str:
        :return:
        """
        has_number=False
        for c in self.password:
            if c.isdigit():
                has_number=True
                break
        return has_number

    def check_letter_exist(self):
        """
        判断字符串中是否含有字母
        :param password_str:
        :return:
        """
        has_letter=False
        for c in self.password:
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
        #实例化密码工具对象
        password_tool=PasswordTool(password)
        password_tool.process_password()

        # 将密码保存到文件中
        f = open('password_3.0.txt', 'a')
        f.write('密码是{}，强度是{}\n'.format(password,password_tool.strength_level))
        f.close()

        if password_tool.strength_level==3:
            print('恭喜！密码强度合格！')

            break
        else:
            print('密码强度不合格!')
            try_times-=1

    if try_times<=0:
        print('尝试次数过多，密码设置失败！')




if __name__ == '__main__':
    main()