import socket
import urllib.request
import urllib.error

#timeout 及异常处理练习
try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')

