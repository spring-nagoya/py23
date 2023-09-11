from flask import Flask
from flask import render_template
from flask import request
import codecs

app = Flask(__name__)

@app.route("/")
def index():
    # ファイルの読み込み
    file = codecs.open("static/messages.txt","r","utf-8")
    
    # テキストデータを取り込み
    post_text = file.readlines()[::-1]
    
    # 開いたファイルを閉じる
    file.close()
    
    # データをHTML側に送る
    return render_template("read_write.html",post_text=post_text)

@app.route("/write",methods=["POST"])
def write():
    
    # HTTPリクエストにより送られた
    # フォームのデータを受け取る
    post_text = request.form["post_text"]
    
    # ファイルにデータを書き込む準備をする
    # w(write):上書き(データを消して書き直す)
    # a(add):追記(最終行にデータを書き込む)
    file = codecs.open("static/messages.txt","a","utf-8")
    
    # 実際にデータを書き込む(\n:改行)
    file.write(post_text + "\n")
    # ファイルを閉じる
    file.close()
    
    # ファイルを読み取り専用モードで、開き直す
    file = codecs.open("static/messages.txt","r","utf-8")
    
    # ファイルを開き直す
    # [::-1]スライス関数
    post_text = file.readlines()[::-1]
    
    # ファイルを閉じる
    file.close()
    
    # 
    return render_template("read_write.html",post_text = post_text)
    



