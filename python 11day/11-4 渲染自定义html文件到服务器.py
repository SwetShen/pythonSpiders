#如果需要显示指定的html文件，则需要render_template工具

from flask import Flask,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app,resources="/*")

@app.route("/")
def hello():
    # 当前目录下
    # 1、在flask项目下，如果要放置html文件，则需要自定义一个templates的文件夹，进行放置
    # 默认情况下，“templates/疫情大数据页面.html”

    # 2、如果要放置js文件，则需要定义一个static的文件夹，进行放置。
    # 3、修改html 中script引入的js的相对路径地址（加上/static）
    return render_template("疫情大数据页面.html")

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000,debug=True)





