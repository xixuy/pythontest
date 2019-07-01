"""
    功能：把字典中的值存到列表中
"""


def main():
    content = [
                    {
                        'date':'2019-05-01',
                        'count':{
                            '湖南':389,
                            '浙江':2694,
                            '广西':1673
                        },
                        'col':{
                            '湖南': 2200,
                            '浙江': 7987,
                            '广西': 2673
                        },
                        'art':{
                            '湖南': 3019,
                            '浙江': 13574,
                            '广西': 6094
                        }
                    },
                    {
                        'date': '2019-05-01',
                        'count': {
                            '湖南': 389,
                            '浙江': 2694,
                            '广西': 1673
                        },
                        'col': {
                            '湖南': 2200,
                            '浙江': 7987,
                            '广西': 2673
                        },
                        'art': {
                            '湖南': 3019,
                            '浙江': 13574,
                            '广西': 6094
                        }
                    }
                ]

    key = []
    values = []
    for i in content:
        items = i.items()
        for item in items:
            key.append(item[0])
            values.append(item[1])

    print(key)
    print(values)


if __name__ == '__main__':
    main()