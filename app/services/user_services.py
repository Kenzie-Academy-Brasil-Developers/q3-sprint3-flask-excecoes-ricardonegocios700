from flask import request
import os
from os import getenv
#import ujson as json
from json import dump, load

from app.exc import FieldTypeError
from app.model.user import User

LOCATION_JSON_DATA = getenv('LOCATION_JSON_DATA')

def new_database_json() -> None:
    os.system("mkdir ./app/database")
    new_file = []
    with open(LOCATION_JSON_DATA, 'w') as json_content:
        dump(new_file, json_content, indent=4)

def valid_user_name(nome) -> str:
    novo_nome = ""
    for n in nome.split():
        novo_nome += " " + n.capitalize()
    return novo_nome.strip()

def next_id() -> int:
    database = User.read_json()
    result = 0
    for i in database:
        if i["id"] > result:
            result = i["id"]
    return result + 1

def email_exist(email: str) -> bool:
    database = User.read_json()
    for i in database:
        if i["email"] == email:
            return True
    return False

def valid_json_file(parametros) -> None:
    if not os.path.exists(LOCATION_JSON_DATA):
        new_database_json()

def valid_fields(name: str, email: str) -> bool:
    if type(name) == str and type(email) == str:
        return True
    raise FieldTypeError

def show_users() -> str:
    if not os.path.exists(LOCATION_JSON_DATA):
        new_database_json()

    if os.stat(LOCATION_JSON_DATA).st_size==0:
        os.remove(LOCATION_JSON_DATA)
        new_database_json()
    return {"data": User.read_json()}, 200

#TODO refatorar: faltou onde executar as validações
#TODO a class fica na model, e opera o DB
#TODO o services auxilia a model, com metodos statics (eu acho)
#TODO faltou o controller, que faz a regra de negócios (eu acho)
def new_user():
    parametros = request.get_json()
    try:
        valid_fields(parametros["nome"], parametros["email"])
    except FieldTypeError:
        raise

    valid_json_file(parametros)
    parametros["nome"] = valid_user_name(parametros["nome"])
    parametros["email"] = parametros["email"].upper()
    parametros["id"] = next_id()

    if email_exist(parametros["email"]):
        return {"error": "User already exists."}, 409

    json_list = User.read_json()
    json_list.append(parametros)
    User.new_user(json_list)
    return {"data": User.read_json()}, 201
