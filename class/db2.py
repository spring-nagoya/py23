from flask import Flask, render_template
# mysql-connector-pythonを読みこむ
import mysql.connector

app = Flask(__name__)


# MySQLへの接続設定を行う関数
def conn_db():
    # DBへの接続オブジェクトを作成
    conn = mysql.connector.connect(
        # MySQLがどこにあるのか
        host = "127.0.0.1",
        # 誰がDBを使うのか
        user="root",
        # DB使用の認証情報
        passwd = "P@ssw0rd",
        # 使用するデータベース名
        db = "py23"
    )

    # 関数を呼び出した先に接続オブジェクトを返す
    return conn


@app.route("/")
def top():

    try:
    # conn_db関数を実行接続オブジェクトを取得
        conn = conn_db()
    # SQLを実行するための処理をコピーする
        cursor = conn.cursor()
    # 実行するSQlの作成
        sql = "select * from t_sample;"

    # SQLの実行(この例ではselect文の実行)
        cursor.execute(sql)

        # fetchall:テーブルからすべてのレコードを取得
        records = cursor.fetchall()


    # SQLを実行するための処理群を破棄する
        cursor.close()
    # SQLの実行結果を確定する    
        return render_template("db2.html", records=records)
    
    # 例外処理
    except(mysql.connector.errors.ProgrammingError) as e:
        print(e)
    



    
