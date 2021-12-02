from flask import Flask
from flask_pymongo import PyMongo


app=Flask(__name__)
app.secret_key = "allen"

app.config["MONGO_URI"]="mongodb+srv://user1:uJEo0dIWpC6s4wc0@dbmsproject.hqrwo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongodb_client=PyMongo(app)
db=mongodb_client.db

from flask_app import route