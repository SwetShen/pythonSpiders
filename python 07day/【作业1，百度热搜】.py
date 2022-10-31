import re
import urllib
from urllib import request

#【作业1，百度热搜中，获取标题、内容描述、热搜指数】。
# https://top.baidu.com/board?tab=realtime
url = 'https://top.baidu.com/board?tab=realtime'

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}

req = request.Request(url,headers=header)
res = request.urlopen(req)

html = res.read().decode('utf-8')
# print(html)

regex = r'''<div class="hot-index_1Bl1a">(.*?)</div>'''

result = re.findall(re.compile(regex,re.S),html)
print(len(result))

regex1 = r'''<div class="c-single-text-ellipsis">(.*?)<.*?'''

result1 = re.findall(re.compile(regex1,re.S),html)
print(len(result1))

regex2 = r'''<div class="hot-desc_1m_jR large_nSuFU .*?">(.*?)a.'''

result2 = re.findall(re.compile(regex2,re.S),html)

data = []
for i in range(len(result)):
    data.append((result[i],result1[i],result2[i]))
print(data)