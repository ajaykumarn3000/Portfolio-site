from flask import Flask, render_template, url_for, redirect, flash, request
from flask_mail import Mail, Message
import json
import random
import os

# This is your test secret API key.


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL_ID = os.environ.get("EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def send_mail(name, email, message):
    msg = Message(f"Portfolio Message!!", sender=EMAIL_ID, recipients=[os.environ.get("ADMIN_MAIL")])
    msg.html = f'''<h3>From: {name}</h3>\n<h3>Email: {email}</h3>\n<h3>Message: {message}</h3>'''
    mail.send(msg)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    with open("static/data.json", mode="r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # send_mail(name, email, message)
        flash("Message sent Successfully!!")
        return redirect(url_for("homepage"))
    return render_template("index.html", data=data)


if __name__ == '__app__':
    app.run(debug=True)
