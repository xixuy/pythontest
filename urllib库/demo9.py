"""
功能：将字典参数序列化为GET参数
"""

from urllib.parse import urlencode

params={
    'name':'tom',
    'age':22
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)