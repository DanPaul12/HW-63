from flask import request, json, jsonify
from models.schemas import user_schema, users_schema
from services import userService
from utils.util import role_required

def save():
    user_data = user_schema.load(request.json)
    save_user = userService.save(user_data)
    return user_schema.jsonify(save_user)

@role_required('boss')
def find_all():
    users = userService.find_all()
    return users_schema.jsonify(users), 200

def login_user():
    user = request.json
    login = userService.login_user(user['username'], user['password'])
    if login:
        return jsonify(login), 200
    else:
        resp={
            "message":"failure"
        }
        return jsonify(resp), 400