import re
from urllib import request

header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}

url = 'https://www.meishij.net/chufang/diy/?&page=1'

req = request.Request(url,headers=header)

response = request.urlopen(req)

html = response.read().decode('utf-8')

# print(html)

regex = re.compile(r'class="big">.*?<img class="img" alt="(.*?)" src="(.*?)">',re.S)

result = re.findall(regex,html)
print(result)


