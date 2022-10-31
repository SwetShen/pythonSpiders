#如何解决跨域问题
# flask_cors : pip install flask_cors 解决flask跨域问题的插件
# 导入flask_cors中的CORS函数
# CORS 应用到flask的整个项目
# app.run(应用的地址，端口，是否启用DEBUG模式)

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
#CORS(app=项目名称,resources=解决的route的范围（*：任意字符串）)
CORS(app=app,resources="/*")

@app.route("/")
def hello():
    # 服务器返回给浏览器的内容
    return '<h1>你正在访问老师的服务器...</h1>'

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000,debug=True)





