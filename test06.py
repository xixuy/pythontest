#正则表达式

import re

a = 'eew \' eawr,2 fd\n sa:21'

b = re.sub(r'[\':\s ,]*', '', a)  # 前面是正则表达式，匹配多种字符（串）
print(a)
print(b)
print('+'*30)


#替换字典中的括号
dict={
    'a':1,
    'b':2,
    'c':3
}
#将字典转化为字符串
c=str(dict)
#替换字符串中想要替换的字符
dict_new=re.sub(r'^{|}$','',c)
print(dict)
print(dict_new)


m='@bg北京2019-05'
n=m[3:]
w=m[1:3]
if w=='kj':
    t=w.replace(w,'33')
elif w=='bg':
    t = w.replace(w, '03')

print(n)
print(w)
print(t)

time="2019-05-12 03:00:05"
time01=str(time)
time02=time01[0:10]
print(time02)

