# Importa las librerías necesarias
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración de la base de datos
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2',salt_length=16)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class ConversionTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    original_extension = db.Column(db.String(10), nullable=False)
    destination_extension = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), default='uploaded')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con el Usuario
    user = db.relationship('User', backref=db.backref('conversion_tasks', lazy=True))
