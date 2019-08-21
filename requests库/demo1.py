"""
功能：requests库的基本用法
"""

import requests

r=requests.get('http://www.baodu.com')
print(type(r))
print(r.status_code)
print(r.headers)
# print(r.text)
print(r.cookies)