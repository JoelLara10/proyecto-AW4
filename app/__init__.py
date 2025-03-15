from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import pymysql

pymysql.install_as_MySQLdb()

# Crear la instancia de la app Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root@localhost/conexionmysql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos y las migraciones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
