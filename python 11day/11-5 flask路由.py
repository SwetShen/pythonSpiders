#如果需要显示指定的html文件，则需要render_template工具

from flask import Flask,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app,resources="/*")

#http://192.168.1.16:5000
@app.route("/")
def default():
    #redirect 重定向 在默认情况下只打开hello页面
    return app.redirect("/hello")

#http://192.168.1.16:5000/hello
@app.route("/hello")
def hello():
    return "<img src='static/img/a.png'>"

@app.route("/info")
def info():
    return "<h2>这是内容页面</h2><a href='/hello'>跳转到hello页面</a>"

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000,debug=True)





