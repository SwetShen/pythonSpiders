
#1、 安装flask ：pip install flask
#2、 使用Flask建立基础服务器

from flask import Flask

# 建立一个服务器对象
# __name__ 当前python文件运行的任务是服务器

app = Flask(__name__)

# 路由:/ + 路由的相关函数
@app.route("/")
def hello():
    # 服务器返回给浏览器的内容
    return '<h1>你好啊</h1>'

# 通过主线程将服务器运行起来
if __name__ == "__main__":
    #服务器运行起来  默认端口是5000
    #服务器的默认地址是本机地址，localhost/192.168.1.16
    # http://localhost:5000  http://192.168.1.16:5000
    # 如何获取自己电脑的地址 WIN+R 启动运行窗口 输入cmd回车，再输入ipconfig 找到以太网地址
    app.run()





