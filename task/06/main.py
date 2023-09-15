from flask import Flask ,redirect ,url_for,render_template,request,session
from datetime import timedelta


app = Flask(__name__)

app.secret_key="abcdefghijklmn"

app.permanent_session_lifetime = timedelta(minutes=3)

@app.route("/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form.get("id")
        session["id"] = user
        
        return redirect(url_for("login_"))
    else:
        if "id" in session:
            return redirect(url_for("login_"))
    return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login_():
    if "id" in session:
        return render_template("view.html", id=session["id"])
    return render_template("login.html")

@app.route("/logout",methods=["GET","POST"])
def logout():
    session.pop("id",None)
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)