from flask import Flask, jsonify

from app.models.user import User
from app.services.user_services import get_request_new
from app.exc.field_type_error import FieldTypeError

app = Flask(__name__)


@app.get("/user")
def list_users():
    return {"msg": User.show_users()}, 200

@app.post("/user")
def add_user():
    params = get_request_new()
    user = User(nome= params['nome'], email= params["email"])
    try:
        result = user.save_user(params)
    except FieldTypeError as e:
        return jsonify(e.message), e.code

    return {result["type"]: result["msg"]}, result["cod"]
