import os
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
from dotenv import load_dotenv


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

load_dotenv()

MYNAME = os.getenv('MYNAME')
USEREMAIL = os.getenv('USEREMAIL')
USERPASSWORD = os.getenv('USERPASSWORD')

@app.route('/')
@app.route('/home')
def home():
    context = None
    if session.get("infosession"):
        context = session['infosession']
    return render_template('home/homepage.html', context={
        'session':context,
        'user':MYNAME
    })


@app.route('/rank')
def rank():
    context = None
    if session.get("infosession"):
        context = session['infosession']
    return render_template('rankers/ranks.html', context={
        'session':context,
        'user':MYNAME
    })


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email, pwd = request.form['email'], request.form['pwd']
        if email == USEREMAIL and pwd == USERPASSWORD:
            #session['infosession'] = f"{email}_{pwd}"
            return redirect(url_for('home'))
    return render_template('account/signup.html')


@app.route('/logout')
def logout():
    if session.get("infosession"):
        session.pop('infosession', None)
    return redirect(url_for('home'))