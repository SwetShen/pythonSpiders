
from flask import Flask
from flask_cors import CORS
# import sqlite3
#对列表、字典、元组、对象 信息进行解析
from flask import jsonify
from dbtool import excute


app = Flask(__name__)
CORS(app=app,resources="/*")

@app.route("/")
def default():
    return app.redirect("/book")

@app.route("/book")
def hello():
    #访问数据库
    # conn = sqlite3.connect('douban.db')
    # cur = conn.cursor()
    # books = cur.execute('select * from book')
    # result = books.fetchall()

    return jsonify(excute('select * from book'))


if __name__ == "__main__":
    #取消flask默认的unicode编码方式
    app.config['JSON_AS_ASCII']=False
    app.run("0.0.0.0",port=5000,debug=True)





