"""
功能：URL的识别和分段
"""

from urllib.parse import urlparse

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)