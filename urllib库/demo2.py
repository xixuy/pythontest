import urllib.request
import urllib.parse

"""
功能：data参数案例
"""
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=1)
print(response.read())