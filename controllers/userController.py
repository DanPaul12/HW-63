from flask import request, json, jsonify
from models.schemas import user_schema
from services import userService

def save():
    user_data = user_schema.load(request.json)
    save_user = userService.save(user_data)
    return user_schema.jsonify(save_user)