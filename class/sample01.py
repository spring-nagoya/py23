from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/index",methods=["GET"])
def index():
    flg = request.args.get("flg")
    return render_template("sample01.html", flg=flg)


@app.route("/loop")
def loop():
    
    fruits_list = ["apple","lemon","banana","melon"]
    user_dic = {"ユーザー1":"User01","ユーザー2":"User02","ユーザー3":"User03"}
    
    return render_template("sample01-1.html",fruits_list=fruits_list,user_dic=user_dic)


