from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import datetime #日時を管理するオブジェクト


app = Flask(__name__)

@app.route("/")
def index():
    
    # make_response関数でCookieにデータを入れる器を作る
    response = make_response("**Cookieの練習**")
    
    # Cookieに関する設定
    # 2週間 = 1209600秒
    max_age = 60 * 60 * 24 * 14 #秒＊分＊時間＊日
    
    # データを保存する期限を決める
    # datetimeオブジェクト:日付や時間を管理する部品
    # timestamp関数:日時を秒数に変換
    expires = int(datetime.datetime.now().timestamp())+max_age
    
    # set_cookie関数:ブラウザに覚えさせるCookieを作成する。
    # key:データの名称
    # value:データの値
    # max_age:Cookieの保存期間
    # expires:Cookieの保存期限
    # path:Cookieの使用パスを制限する
    # domain:別のwebサイトにCookieを送るときに使用
    # secure:True(HTTPSであればOK),False(http/https問わずOK)
    # httponly:JavaScriptからCookie情報を参照可能にするか
    response.set_cookie( key='uid' , value="user01" , max_age=max_age , expires=expires , path="/" , domain="127.0.0.1" , secure=True , httponly=False)
    
    # ブラウザ側に設定した応答情報であるresponseオブジェクトを渡す
    return response

@app.route("/show_cookie")
def show_cookie():
    
    # cookieの中から指定したキーの情報を取り出す
    
    uid = request.cookies.get('uid', None)

    return render_template("cookie.html", uid=uid)