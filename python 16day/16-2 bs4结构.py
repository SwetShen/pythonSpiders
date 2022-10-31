import bs4
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
}

url = 'https://www.baidu.com'
html = requests.get(url=url,headers=headers).text
soup = bs4.BeautifulSoup(html,'html.parser')

# 根据id属性找到对应的标记
# result = soup.find('div',id='s-top-left')

# 根据class属性找到对应的标记
result = soup.find('div',class_='s-top-left-new s-isindex-wrap')

# 如果用“.标记”的方式，只能找到第一个标记
# print(result.a)

# 找到所有的标记
# alist = result.find_all('a')
# for item in alist:
#     print(item.string)

#find_all 也可以加id和class属性
alist = result.find_all('a',class_='mnav c-font-normal c-color-t')
for item in alist:
    print(item.string)