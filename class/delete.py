from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

import mysql.connector


# MySQLへの接続設定を行う関数
def conn_db():
    # DBへの接続オブジェクトを作成
    conn = mysql.connector.connect(
        # MySQLがどこにあるのか
        host="127.0.0.1",
        # 誰がDBを使うのか
        user="root",
        # DB使用の認証情報
        passwd="P@ssw0rd",
        # 使用するデータベース名
        db="py23",
    )
    return conn


@app.route("/")
def index():
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return render_template("index.html", record=result)


@app.route("/delete", methods=["GET"])
def delete():
    conn = ""
    cursor = ""
    try:
        id = request.args.get("id")
        conn = conn_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM T_sample WHERE id= {0}".format(id))
        conn.commit()
    except mysql.connector.Error as e:
        print(e)

    # SQLインジェクション対策の為に、SQLパラメータを使用したパターン
    # sql = "DELETE FROM T_sample WHERE id= %s"
    # executeメソッドの第二引数にタプル型で値を渡すことで、SQLパラメータに値を当てはめることが可能。
    # ただし、パラメータが1つでも最後にカンマを付ける必要がある。
    # cursor.execute(sql, (id,))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return redirect(url_for("index"))
