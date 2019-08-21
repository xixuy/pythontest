"""
功能：GET请求
"""

import requests

data={
    'name':'jams',
    'age':22
}
r=requests.get('http://httpbin.org/get',params=data)
print(r.text)