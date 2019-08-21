"""
功能：判断网页是否可以抓取
"""

from urllib.robotparser import RobotFileParser

rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))