from flask import Flask 

# 別のページ(複数)に転送する為の機能
from flask import redirect

# URL特定用の機能
from flask import url_for
from flask import render_template
from flask import request

# セッションを使用するための機能
from flask import session

# マイクロ秒まで検知する正確な時間を測る為の機能
from datetime import timedelta


app = Flask(__name__)

# セッション情報を暗号化する為のパスワード
app.secret_key="abcdefghijklmn"

# セッションの保存期間を3分間に設定
app.permanent_session_lifetime = timedelta(minutes=3)

@app.route("/", methods=["POST","GET"])
def login():
    # フォームからPOSTメソッドを使って送信されたか
    if request.method == "POST":
        # セッション情報の作成
        session.permanent = True
        # login.htmlから送られた情報を受け取る
        user = request.form.get("id")
        # セッションという箱にidという名前の
        # 仕切りを作ってデータを保存する
        session["id"] = user
        
        # login_関数に転送する
        return redirect(url_for("login_"))
    # データが送られた場合の処理
    else:
        if "id" in session:
            return redirect(url_for("login_"))
    return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login_():
    # idという入れ物があれば
    if "id" in session:
        return render_template("login-1.html", id=session["id"])
    return render_template("login.html")

# セッション情報の削除を行う関数
@app.route("/logout",methods=["GET","POST"])
def logout():
    session.pop("id",None)
    # セッションの強制削除を実行する
    session.clear()
    return redirect("/")