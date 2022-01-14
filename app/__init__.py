from flask import Flask #, jsonify, request
#from os import getenv
from kenzie import show_users, new_user


app = Flask(__name__)

@app.get("/user")
def list_users():
    return show_users()

@app.post("/user")
def add_user():
    return new_user()

