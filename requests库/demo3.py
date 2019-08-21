"""
功能，抓取网页
"""

import requests
import re

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
r=requests.get('https://www.zhihu.com/explore',headers=headers)
#这一行不明白
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
title=re.findall(pattern,r.text)
print(title)