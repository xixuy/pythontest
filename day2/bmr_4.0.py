"""
    功能：BMR计算器
    版本：4.0
    日期：2019/06/20
    增加功能：异常处理
    知识点：异常处理机制
"""


def main():
    """
    主函数
    :return:
    """
    y_or_n = input('是否退出程序(y/n)?')

    while y_or_n != 'y':

        input_str=input('性别 体重(kg) 身高(cm) 年龄：')
        #分割字符串
        str_list=input_str.split(' ')
        try:
            gender = str_list[0]
            weight = float(str_list[1])
            height=float(str_list[2])
            age=int(str_list[3])
            if gender == '男':
                # 男性
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
            elif gender == '女':
                # 女性
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 65
            else:
                bmr = -1
            if bmr != -1:
                print('基础代谢率：%d大卡' % (bmr))
            else:
                print('暂不支持该性别')
        except ValueError:
            print('请输入正确的信息！')
        except IndexError:
            print('输入的信息过少！')
        except:
            print('程序异常！')

        y_or_n = input('是否退出程序(y/n)?')


if __name__ == '__main__':
    main()
