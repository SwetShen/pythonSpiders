
from urllib import request
#请求头
#用户协议代理
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}

url = 'https://www.baidu.com'
# 协议请求格式，加入请求头
req = request.Request(url,headers=header)

response = request.urlopen(req)

print(response.read().decode('utf-8'))

