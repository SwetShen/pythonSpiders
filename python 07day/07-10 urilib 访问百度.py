#request 请求
from urllib import request

url = 'https://www.baidu.com'

#res: response 响应结果
# 由于代码访问网站，是通过框架本身，因此会被服务器识别出代码访问。
res = request.urlopen(url)

#read()获取响应中的内容
print(res.read())

print(res.geturl()) #获取主机地址  https://www.baidu.com
print(res.getcode()) #获取请求状态码  200(OK) 502 404 503...
print(res.info()) #获取响应头 了解

#为什么代码不能访问网站，浏览器可以？
