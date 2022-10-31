import re
import time
import random
import urllib
from urllib import request,parse

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}

url = 'https://book.douban.com/latest?subcat=' + parse.quote("文学")
#"%E6%96%87%E5%AD%A6" URL编码 一般用于搜索时文字的编码
# print(parse.quote('文学'))


req = request.Request(url,headers=header)

response = request.urlopen(req)

html = response.read().decode('utf-8')

regex = re.compile(r'''<div class="media__img">
                <a href="(.*?)"><img.*?src="(.*?)".*?''',re.S)
links = re.findall(regex,html)
print(links)
# 通过上一步的链接地址,继续访问每一个电影的信息

num = 0
for item in links:
    # 1分钟之内 不能超过30~40访问
    # 随机睡眠1到4秒
    n = 1 + random.random() * 3
    time.sleep(n)
    print("-"*5,"爬取第" + str(num) + "次")
    res = request.urlopen(request.Request(item[0],headers=header))
    book_html = res.read().decode('utf-8')
    with open("books/书籍" + str(num) + ".txt",mode='a+',encoding='utf-8') as f:
        f.write(book_html)
        f.close()
    num += 1

