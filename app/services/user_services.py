from flask import request
import os
from os import system, getenv
import ujson as json
from json import dump, load
from app.exc import ArquivoError

LOCATION_JSON_DATA = getenv('LOCATION_JSON_DATA')

def new_database_json() -> None:
    os.system("mkdir ./app/database")
    new_file = []
    with open(LOCATION_JSON_DATA, 'w') as json_content:
        dump(new_file, json_content, indent=4)

def read_database_json() -> str:
    try:
        with open(LOCATION_JSON_DATA, 'r') as json_file:
            return load(json_file)
    except:
        return {"msg": "tratar erros aqui"}

def show_users() -> str:
    if not os.path.exists(LOCATION_JSON_DATA):
        new_database_json()

    if os.stat(LOCATION_JSON_DATA).st_size==0:
        os.remove(LOCATION_JSON_DATA)
        new_database_json()

    return {"data": read_database_json()}, 200

def valid_fields(name: str, email: str) -> bool:
    if type(name) == str and type(email) == str:
        return True
    return False

def valid_user_name(nome) -> str:
    novo_nome = ""
    for n in nome.split():
        novo_nome += " " + n.capitalize()
    return novo_nome.strip()

def next_id() -> int:
    database = read_database_json()
    result = 0
    for i in database:
        if i["id"] > result:
            result = i["id"]
    return result + 1

def email_exist(email: str) -> bool:
    database = read_database_json()
    for i in database:
        if i["email"] == email:
            return True
    return False
    

def new_user():
    if not os.path.exists(LOCATION_JSON_DATA):
        new_database_json()
    raise ArquivoError("não existe o arquivo de banco de dados")
        
    # parametros = request.get_json()
    # if not valid_fields(parametros["nome"], parametros["email"]):
    #     return (
    #         {"wrong fields": 
    #         f"[{'nome': 'integer'}, {'email': 'dictionary'}]"}
    #     ), 400
    # parametros["nome"] = valid_user_name(parametros["nome"])
    # parametros["email"] = parametros["email"].upper()
    # parametros["id"] = next_id()

    # if email_exist(parametros["email"]):
    #     return {"error": "User already exists."}, 409
    # json_list = read_database_json()
    # json_list.append(parametros)
    # with open(LOCATION_JSON_DATA, 'w') as json_content:
    #     dump(json_list, json_content, indent=4)
    # return {"data": read_database_json()}, 201
