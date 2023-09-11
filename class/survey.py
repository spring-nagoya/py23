from flask import Flask , render_template , request
import codecs
import datetime

app = Flask(__name__)

@app.route("/")
def survey():
    return render_template("survey.html")

@app.route("/check",methods=["POST"])
def check():
    name = request.form["name"]
    mail = request.form["mail"]
    comment = request.form["comment"]
    
    return render_template("check.html",name=name,mail=mail,comment=comment)


