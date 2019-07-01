"""
    功能：把字典中的值存到列表中
"""

def main():
    content = [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 100},
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 90},
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 10},
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 80}]
    print(type(content))

    key=[]
    values=[]
    for i in content:
        items=i.items()
        for item in items:
            key.append(item[0])
            values.append(item[1])


    print(key)
    print(values)


if __name__ == '__main__':
    main()