import urllib.request

response=urllib.request.urlopen('http://www.python.org')
print(response.status)  #获取相应状态码
print(response.getheaders()) #获取相应的头信息
print(response.getheader('Server'))
# print(response.read().decode('utf-8'))