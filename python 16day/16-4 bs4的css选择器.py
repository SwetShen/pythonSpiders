import bs4
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
    ,'Content-Type': 'text/html,charset=utf-8'
}

url = 'http://www.weather.com.cn/weather15d/101040100.shtml'

# 获取这个响应方式的编码
code = requests.get(url=url,headers=headers).encoding
# print(code)#ISO-8859-1

# 对获取内容进行解码。
html = requests.get(url=url,headers=headers).text.encode(code).decode('utf-8')
soup = bs4.BeautifulSoup(html,'html.parser')

# 通过选择器找出的内容是一个列表
ul = soup.select('.t.clearfix')
# print(ul)

spans = ul[0].select('li>span')
# print(spans)

for span in spans:
    print(span.string)




