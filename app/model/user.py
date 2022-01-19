from json import dump, load
from os import getenv

from app.exc.field_type_error import FieldTypeError

LOCATION_JSON_DATA = getenv('LOCATION_JSON_DATA')

class User:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @classmethod
    def read_json(cls):
        with open(LOCATION_JSON_DATA, 'r') as json_file:
                return load(json_file)

    @staticmethod
    def new_user(json_list):
        with open(LOCATION_JSON_DATA, 'w') as json_content:
            dump(json_list, json_content, indent=4)

    