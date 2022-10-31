import re
from urllib import request

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}

url = 'http://www.weather.com.cn/weather15d/101040100.shtml'

req = request.Request(url,headers=header)

response = request.urlopen(req)

html = response.read().decode('utf-8')

# print(html)

regex = re.compile(r'''>
<span class="time">(.*?)</span>
<big class=".*?"></big>
<big class=".*?"></big>
<span class="wea">(.*?)</span>
<span class="tem"><em>(.*?)</em>/(.*?)</span>
<span class="wind">(.*?)</span>
<span class="wind1">(.*?)</span>.*?''',re.S)

result = re.findall(regex,html)
print(result)


