from flask import Blueprint, request, jsonify
from src.models.repositories.user_repository import UserRepository
from src.drivers.jwt_handler import encode_jwt

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserRepository.find_user_by_username(username)
    if user and UserRepository.verify_password(user['password'], password):
        token = encode_jwt(user['id'], user['username'])
        return jsonify({'token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401
