from urllib.parse import urlencode,parse_qs,parse_qsl

params={
    'name':'germey',
    'age':22
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)
print('='*50)
#反序列化

query='name=germey&age=22'
#将参数转化为字典
print(parse_qs(query))
print('='*50)
#将参数转化为元组组成的列表
print(parse_qsl(query))