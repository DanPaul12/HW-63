from datetime import timedelta, datetime
import jwt
import os
from dotenv import load_dotenv
from flask import request, jsonify, current_app
from functools import wraps

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def encode_token(role_names):
    payload={
        'exp': int((datetime.now() + timedelta(days=1)).timestamp()),  # Expiration time
        'iat': int(datetime.now().timestamp()), 
        'roles': role_names
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print(SECRET_KEY)
    print('token sent to postman', token)
    return token