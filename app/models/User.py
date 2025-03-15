from app.config import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'usuarios'  # Nombre correcto de la tabla

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Aumenta el tamaño para contraseñas hash

    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = generate_password_hash(password)  # Guarda la contraseña encriptada

    def check_password(self, password):
        return check_password_hash(self.password, password)  # Verifica la contraseña
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }
