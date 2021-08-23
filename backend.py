import time
import six
from werkzeug.exceptions import Unauthorized
from jose import JWTError, jwt
from datetime import datetime, timedelta
from flask import request
from database.CRUD import data_table_backend, eMail_backend, config_table_backend

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'config_table_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def _current_timestamp() -> int:
    return int(time.time())


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def generate_token(sub):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(sub)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def backend_read(method):
    try:
        select_result = {
            "data_table": data_table_backend,
            "config_table": config_table_backend,
            "eMail": eMail_backend
        }.get(method).read()
        result = {"result": "success", "data": select_result}
        return result
    except Exception as e:
        result = {"result": str(e), "data": [], "JWT_token": ""}
        return result


def backend_create(method, frontend_data):
    try:
        config = config_table_backend.read("1")
        config[0]["Change"] = "1"
        config_table_backend.update(config[0])
        frontend_data["ID"] = {
            "data_table": data_table_backend,
            "config_table": config_table_backend,
            "eMail": eMail_backend
        }.get(method).get_count()+1
        print(frontend_data)
        {
            "data_table": data_table_backend,
            "config_table": config_table_backend,
            "eMail": eMail_backend
        }.get(method).create(frontend_data)
        result = {"result": "success"}
        return result
    except Exception as e:
        result = {"result": str(e), "JWT_token": ""}
        print(result)
        return result


def backend_update(method, frontend_data):
    try:
        config = config_table_backend.read("1")
        config[0]["Change"] = "1"
        config_table_backend.update(config[0])
        print("change")
        {
            "data_table": data_table_backend,
            "config_table": config_table_backend,
            "eMail": eMail_backend
        }.get(method).update(frontend_data)
        result = {"result": "success"}
        return result
    except Exception as e:
        result = {"result": str(e), "JWT_token": ""}
        print(result)
        return result


def data_table_read():
    method = "data_table"
    return backend_read(method)


def data_table_create():
    method = "data_table"
    User_data = request.json
    return backend_create(method, User_data)


def data_table_update():
    method = "data_table"
    User_data = request.json
    return backend_update(method, User_data)


def eMail_read():
    method = "eMail"
    return backend_read(method)


def eMail_create():
    method = "eMail"
    User_data = request.json
    return backend_create(method, User_data)


def eMail_update():
    method = "eMail"
    User_data = request.json
    return backend_update(method, User_data)


def config_table_read():
    method = "config_table"
    print(request.json)
    return backend_read(method)


def config_table_create():
    method = "config_table"
    User_data = request.json
    return backend_create(method, User_data)


def config_table_update():
    method = "config_table"
    User_data = request.json
    return backend_update(method, User_data)
