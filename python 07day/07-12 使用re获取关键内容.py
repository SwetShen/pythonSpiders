import re
from urllib import request

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}

url = 'https://www.baidu.com'

req = request.Request(url,headers=header)

response = request.urlopen(req)

html = response.read().decode('utf-8')

# 拿到html之后如何操作
# .* : 0到多个任意字符
# ? 非贪婪式读取
regex = re.compile(r'<span class="title-content-title">(.*?)</span>')

result = re.findall(regex,html)
print(result)

#【作业1，百度热搜中，获取标题、内容描述、热搜指数】。
# https://top.baidu.com/board?tab=realtime

#【作业2，天气预报网站中，日期，天气状况、温度、风向】
# http://www.weather.com.cn/weather15d/101040100.shtml