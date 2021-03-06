# coding: utf-8
'''
    admin_required.py
    ~~~~~~~~~~~~~~~~~

        token管理员权限装饰器
'''

from functools import wraps
from flask import request


def admin_required(Model):
    def admin_decorator(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token_header = request.headers.get('authorization')
            token = token_header[6:]
            if token:
                user = Model.verify_auth_token(token)
                if user.is_admin():
                    return f(*args, **kwargs)
                else:
                    abort(403)
            else:
                abort(403)
        return decorator
    return admin_decorator

