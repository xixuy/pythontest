"""
功能：抓取二进制数据
"""

import requests
r=requests.get('https://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(r.content)
