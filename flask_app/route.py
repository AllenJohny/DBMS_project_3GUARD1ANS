from flask_app import app
from flask import render_template
from .forms import TodoForm

@app.route("/")
def index():
    return render_template("file.html")