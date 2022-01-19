import json
import os
from unicodedata import name
from flask import request
from os import getenv
from json import dump

from app.exc import FieldTypeError

DB_JSON = getenv("LOCATION_JSON_DATA")


def new_database_json() -> None:
    os.system("mkdir app/database")
    new_file = []
    with open(DB_JSON, 'w') as json_content:
        dump(new_file, json_content, indent=4)

def get_request_new() -> json:
    return request.get_json()
        
def valid_user_name(nome) -> str:
    new_nome = ""
    for n in nome.split():
        new_nome += " " + n.capitalize()
    return new_nome.strip()

def valid_fields(nome: str, email: str) -> bool:
    if (type(nome) != str or type(email) != str):
        raise FieldTypeError(type(nome).__name__, type(email).__name__)
    return True
    
def valid_params(params) -> json:
    valid_fields(params["nome"], params["email"])
    params["email"] = params["email"].lower()
    params["nome"] = valid_user_name(params["nome"])
    return params