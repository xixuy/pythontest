"""
    功能：把字典中的值存到列表中
"""


def main():
    content = {
        'result':[
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
                        'date': '2019-05-02',
                        'count': {
                            '湖南': 399,
                            '浙江': 2794,
                            '广西': 1473
                        },
                        'col': {
                            '湖南': 2106,
                            '浙江': 8957,
                            '广西': 2573
                        },
                        'art': {
                            '湖南': 3819,
                            '浙江': 13773,
                            '广西': 6397
                        }
                    }
                ]
            }

    data=content['result']
    dates=[]
    counts=[]
    cols=[]
    arts=[]
    hunancols=[]
    zhejcols=[]
    guangxcols=[]
    for i in data:
        # print(i)
        date=i['date'] #取出字典中的日期
        dates.append(date) #把所有的日期放到列表中

        col=i['col']
        cols.append(col)
        # items = cols.items()

        count = i['count']
        counts.append(count)

        art=i['art']
        arts.append(art)

    for item in cols:
        hunan = item['湖南']
        zhejiang = item['浙江']
        guangxi = item['广西']
        hunancols.append(hunan)
        zhejcols.append(zhejiang)
        guangxcols.append(guangxi)

    print(hunancols)
    print(zhejcols)
    print(guangxcols)
    print(counts)
    print(cols)
    print(arts)
    print(dates)


if __name__ == '__main__':
    main()