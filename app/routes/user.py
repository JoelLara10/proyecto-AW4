from flask import Blueprint, jsonify, request
from app.controllers.userController import get_all_users, create_user, login_user

user_bp = Blueprint('users', __name__)
@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_users()
    return jsonify(user)

@user_bp.route('/', methods = ['POST'])
def user_store():
    data = request.get_json()
    email = data.get('email') 
    name = data.get('name')
    password = data.get('password')
    print(f"NAME {name} --- email {email}")
    new_user = create_user(name, email, password)
    return jsonify(new_user)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return login_user(email, password)