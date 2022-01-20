import os
from os import getenv
from json import load, dump
from textwrap import indent

from app.services.user_services import new_database_json, get_request_new, valid_params

DB_JSON = getenv("LOCATION_JSON_DATA")

class User:
    def __init__(self, nome, email) -> None:
        self.nome = nome
        self.email = email

    @staticmethod
    def show_users():
        try:
            if os.stat(DB_JSON).st_size==0:
                os.remove(DB_JSON)
        except:
            ...
        if not os.path.exists(DB_JSON):
           new_database_json()
        with open(DB_JSON, 'r') as json_file:
            return load(json_file)

    @staticmethod
    def next_id():
        database = User.show_users()
        result = 0
        for i in database:
            if i["id"] > result:
                result = i["id"]
        return result + 1

    @staticmethod
    def emails_exist(email):
        database = User.show_users()
        for i in database:
            if i["email"].lower() == email.lower():
                return True
        return False

    def save_user(self, params):
        params = valid_params(params)
        if self.emails_exist(params['email']):
            #TODO verificar mensagem de email existente
            return {"error": "User already exists.", "cod": 409}
        params['id'] = self.next_id()
        result = {"msg": [{"id": params["id"], "nome": params['nome'], "email": params['email']}], "cod": 201}
        dbase_json = self.show_users()
        dbase_json.append(params)
        with open(DB_JSON, "w") as json_file:
            dump(dbase_json, json_file, indent=4)
        return result
    