#flaskというツールから本体を取り出す。
from flask import Flask
from flask import render_template
from flask import request

#__name__ = ファイル名
#webアプリケーション名をindexとする。
app = Flask(__name__)

#http://127.0.0.1:5000というURLでアクセスされたら
#hello_worldという関数が実行される
@app.route("/")

#hello_worldという名前の関数を定義
def hello_world():
    #webブラウザにhello world!という文字を返す
    return "Hello World!"

#http://127.0.0.1:5000/page2/
@app.route("/page2")
def message():
    return "Python + Flask"

# /<name>パラメータをURLに乗せた場合
@app.route("/<name>")
# hello_user関数にはnameという引数が必要
def hello_user(name):
    
    # f:formatの意味(文法の定義)
    # helloという文字列に引数nameの値を結合する
    # "hello{0}".format(name)
    return f"Hello {name}"

# index.htmlを表示するためのルーティング
@app.route("/index")
def view_index():
    # render_template関数
    # 指定したhtmlファイルを表示
    return render_template("index.html" , username="user01")

@app.route("/f_get")
def display_form():
    return render_template("form.html")

@app.route("/form_get", methods=['GET'])
def result_get():
    name = request.args.get('field_name',"")
    return render_template("form_get.html",title="FormからGETで送られたデータ", name=name)

@app.route("/form_post", methods=['POST'])
def result_post():
    name = request.form['field_name2']
    # 受け渡し定義
    pwd = request.form['pwd']
    check = request.form.getlist('check')
    radio = request.form['radio']
    address = request.form['Address']
    memo = request.form['memo']
    
    return render_template("form_get.html",title="FormからPOSTで送られたデータ", name=name, pwd=pwd, check=check, radio=radio, address=address, memo=memo)
