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
# print(html)
soup = bs4.BeautifulSoup(html,'html.parser')

ul = soup.find('ul',class_='t clearfix')
# print(ul)

# findChildren 找到对应标记下的所有的子节点
children = ul.findChildren()
# print(children)

#遍历所有的子节点
# for child in children:
    # print(child.findChildren())
    # for item in child.findChildren():
    #     print(item.string)

    # items = child.findChildren()
    # print(items[0].string)
    # print(items[3].string)

# find\find_all 比起 children parents findChildren() 更方便。
