from flask import *
from flask_app import app
from flask import render_template
#from .forms import Login


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def index():
    return render_template("login.html", title = "login page")

@app.route('/login/success',methods = ['POST', 'GET'])  
def success():  
   if request.method == 'POST':     
    session['Uname']=request.form['Uname']
   return render_template("data.html", Uname=session['Uname'])
