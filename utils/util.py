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

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(' ')[1]
            if not token:
                return jsonify({'message':'token is missing'}), 401
            
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return jsonify({'message':'expired token'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message':'invalid token'}), 400
            
            roles = payload['roles']

            if role != roles:
                return jsonify({'message':'user doesnt have role'}), 403
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator