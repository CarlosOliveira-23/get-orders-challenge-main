from functools import wraps
from flask import request, jsonify
from src.drivers.jwt_handler import decode_jwt


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            payload = decode_jwt(token)
            if payload is None:
                return jsonify({'error': 'Invalid token!'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 401

        return fn(payload, *args, **kwargs)

    return wrapper
