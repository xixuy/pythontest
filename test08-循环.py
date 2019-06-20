

#定义变量
n=100
sum=0
count=1
while count<=n:
    sum =sum+count
    count +=1
print(sum)


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

