"""
功能：反序列化
"""

from urllib.parse import parse_qs,parse_qsl

query='name=tom&age=22'
print(parse_qs(query))
print(parse_qsl(query))