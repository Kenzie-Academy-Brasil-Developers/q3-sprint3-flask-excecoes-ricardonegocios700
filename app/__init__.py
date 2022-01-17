from flask import Flask
from app.services import show_users, new_user


app = Flask(__name__)


@app.get("/user")
def list_users():
    return show_users()

# passar nas anotações
@app.post("/user")
def add_user():
    return new_user()

# # exemplo de como pegar o vlr direto da url
# # passar nas anotações
# @app.get("/user/<string:nome>")
# def add_user(nome):
#     ...