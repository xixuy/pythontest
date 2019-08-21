"""
功能：URL的构造
"""

from urllib.parse import urlunparse

data=['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))