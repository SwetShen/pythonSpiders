# 安装beautifulsoup4 框架
#pip install beautifulsoup4

#使用
import bs4
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
}

url = 'https://www.baidu.com'
# requests.get(url=请求链接,headers=头部)
html = requests.get(url=url,headers=headers).text
# 请求到的网页内容，是自动编译成utf-8格式。
# print(html)

#BeautifulSoup(html文件,'html.parser')
soup = bs4.BeautifulSoup(html,'html.parser')
#soup中的title属性，找到title的标签。
print(soup.title.string)
