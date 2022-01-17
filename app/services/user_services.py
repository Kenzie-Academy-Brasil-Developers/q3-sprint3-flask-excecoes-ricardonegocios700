from flask import request
import os
from os import system, getenv
import ujson as json
from json import dump, load

LOCATION_JSON_DATA = getenv('LOCATION_JSON_DATA')

def new_database_json() -> None:
    os.system("mkdir ./app/database")
    new_file = {"data": []}
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

    return read_database_json(), 200

def new_user():
    parametros = request.get_json()
    json_list = read_database_json()
    json_list.append(parametros)
    with open(LOCATION_JSON_DATA, 'w') as json_content:
        dump(json_list, json_content, indent=4)


## rota /user [POST]
# Ao fazer requisição nessa rota, 
# deverá inserir os dados recebidos no seu database.json 
# e retornar o status 201 CREATED.

# O nome deve ter as primeiras letras maiúsculas 
# e o email deve ser salvo com todas as letras minúsculas;

# Fazer a criação dinâmica do id do usuário, 
# sendo esse dado do tipo int;

# Caso o arquivo database.json não exista, 
# deverá fazer a criação do arquivo 
# e salvar o dado recebido pela requisição.

# Deverá verificar se o email já existe dentro do arquivo database.json, 
# se já existir deverá retornar o status 409 CONFLICT.

# Deverá verificar se os dados recebidos estão com o tipo correto, 
# sendo o nome e email do tipo string, 
# caso o valor dessas chaves seja de algum outro tipo, 
# deverá retornar o status 400 BAD REQUEST.

## REQUISIÇÃO
# {
#     "nome": "nome do usuário",
#     "email": "EXEMPLO@MAIL.COM"
# }

## RETORNO
# {
#     "data": {
#         "email": "exemplo@mail.com",
#         "id": 1,
#         "nome": "Nome Do Usuário"
#     }
# }
# 

## RETORNO USANDO UM EMAIL QUE JÁ EXISTE
# STATUS 409 CONFLICT.
# {
#     "error": "User already exists."
# }
# 

## RETORNO USANDO TIPO DE DADOS INCORRETOS
# deve retornar o tipo de dado enviado e não o que se espera
# EXEMPLO:
# { "nome": 1, "email": {} }

# STATUS 400 BAD REQUEST.
# {
#     "wrong fields": [
#         {
#             "nome": "integer"
#         },
#         {
#             "email": "dictionary"
#         }
#     ]
# }
# 
    return read_database_json(), 201