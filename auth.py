from functools import wraps
from flask import request, abort
from datetime import datetime, timedelta
from jose import JWTError, jwt

from error import HttpError
SECRET_KEY = "testsecret"
ALGORITHM = "HS256"

def generate_jwt_token(user_data={"name":"Mule","role":"admin"}):
    expire_time = datetime.utcnow() + timedelta(minutes=45)
    user_data.update({"exp": expire_time})
    encoded_jwt = jwt.encode(user_data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
def verify_jwt_token(token, user='all'):
    token_array = token.split(' ')[1]
    try:
        payload = jwt.decode(token_array, SECRET_KEY, algorithms=[ALGORITHM])
        if user == 'all' or payload['role'] == user:
            is_authorized = True
        else:
            abort(401)
        return is_authorized

    except JWTError:
        raise HttpError(
            status_code=401,
            detail="Could not validate credentials",
        )

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers['Authorization']
        try:
            payload = verify_jwt_token(token)
        except:
            abort(401)
        return f(payload, *args, **kwargs)

    return wrapper
    

def admin_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = token = request.headers['Authorization']
        try:
            payload = verify_jwt_token(token, "admin")
        except:
            abort(401)
        return f(payload, *args, **kwargs)

    return wrapper
def user_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = token = request.headers['Authorization']
        try:
            payload = verify_jwt_token(token,"user")
        except:
            abort(401)
        return f(payload, *args, **kwargs)

    return wrapper