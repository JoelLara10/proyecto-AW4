from app.models.User import User
from flask import jsonify
from app.config import db
from flask_jwt_extended import create_access_token

def get_all_users():
    try:
        return [ user.to_dict() for user in User.query.all()]    
    except Exception as error:
        print(f"ERROR {error}")
        return jsonify({'msg': 'Error al obtener los usuarios'}), 500
        #return jsonify(error)

def create_user(name, email, password):
    try:
        new_user = User(name, email, password)
    
        db.session.add(new_user)
        db.session.commit()
        
        return new_user.to_dict()

    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg': 'Error al crear el usuario'}), 500


def login_user(email, password):
    try:
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return jsonify({
                'access_token': access_token,
                'user': {
                    'id':user.id,
                    'name':user.name,
                    'email':user.email
                }
            })
        return jsonify({'msg': 'Credenciales invalidas'}), 401

    except Exception as e:
        print(f"ERROR {e}")
    