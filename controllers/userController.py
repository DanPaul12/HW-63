from flask import request, json, jsonify
from models.schemas import user_schema, users_schema
from services import userService

def save():
    user_data = user_schema.load(request.json)
    save_user = userService.save(user_data)
    return user_schema.jsonify(save_user)

def find_all():
    users = userService.find_all()
    return users_schema.jsonify(users), 200