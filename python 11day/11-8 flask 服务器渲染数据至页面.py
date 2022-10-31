
from flask import Flask,render_template
from flask_cors import CORS
from dbtool import excute
from flask import jsonify

app = Flask(__name__)
CORS(app=app,resources="/*")

@app.route("/")
def hello():
    return render_template("疫情大数据页面.html")

@app.route("/map")
def getmapdata():
    return jsonify(excute('select * from info'))

@app.route("/top")
def gettopdata():
    #order by 字段名称 desc（降序）/asc（升序） ：以某个字段排序
    #limit 数字：限制查询多少条
    return jsonify(excute('select * from info order by curConfirm desc limit 3'))

if __name__ == "__main__":
    # 取消flask默认的unicode编码方式
    app.config['JSON_AS_ASCII'] = False
    app.run("0.0.0.0",port=5000,debug=True)





