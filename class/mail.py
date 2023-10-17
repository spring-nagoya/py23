from flask import Flask, render_template, redirect, request, url_for
from sendmail import send_mail
from flask.ext.sendmail import Mail

app = Flask(__name__)

@app.route("/")
def index():
    render_template("send-mail.html")
    
@app.route("/mail/", methods=["POST"])
def func_send_mail(mailForm, mailTo, message):
  # 2FA