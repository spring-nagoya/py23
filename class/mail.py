from flask import Flask, render_template, redirect, request, url_for
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("sendmail.html")


@app.route("/check/", methods=["POST"])
def func_send_mail():
    mailForm = request.form.get("form")
    mailTo = request.form.get("to")
    subject = request.form.get("subject")
    message = request.form.get("message")

    return render_template(
        "mailcheck.html",
        mailForm=mailForm,
        mailTo=mailTo,
        subject=subject,
        message=message,
    )
