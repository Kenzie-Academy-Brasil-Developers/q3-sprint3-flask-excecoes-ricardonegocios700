from flask import send_from_directory, request
import os
from os import system, getenv
import ujson as json
from json import dump

json_path = "./app/database/database.json"
def show_users() -> None:
    if not os.path.exists(json_path):
        os.system("mkdir ./app/database")
        new_file = {"data": []}
        with open(json_path, 'w') as json_content:
            dump(new_file, json_content, indent=4)

    file_open = open(json_path)
    result = file_open.read()
    file_open.close()
        
## rota /user [GET]
# Caso o arquivo database.json não exista, 
# deverá fazer a criação do arquivo colocando uma lista vazia dentro dele 
# e deverá retornar esta lista. O status da rota DEVE ser 200 OK.
# { "data": [] }, 200

# Caso o arquivo database.json exista, mas esteja vazio, 
# deverá fazer a inserção de uma lista vazia e retornar esta lista. 
# O status da rota DEVE ser 200 OK.

# Caso o arquivo database.json exista e estiver populado com dados, 
# deverá retornar os dados contidos dentro dele. 
# O status da rota DEVE ser 200 OK.

    return result

def new_user():
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
    return {"teste": "Estamos em post"}