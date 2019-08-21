
import re

str=' <dd><i class="board-index board-index-1">1</i>'

pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>',re.S)
s=re.findall(pattern,str)
print(s)