"""
功能：Request参数的用法
"""

from urllib import parse, request

url='http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
}
dict={
    'name':'Germey'
}
data=bytes(parse.urlencode(dict),encoding='utf8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf-8'))