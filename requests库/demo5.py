"""
功能：POST请求
"""

import requests
data={
    'name':'jerry',
    'age':22
}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)