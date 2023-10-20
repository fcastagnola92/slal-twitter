from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.models import db, User

user_views = Blueprint('user_views', __name__)

@user_views.route('/signup', methods=['GET'])
def get():
    return 'Hola user views'

@user_views.route('/signup', methods=['POST'])
def post():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'El nombre de usuario o el correo electrónico ya existen'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario creado exitosamente'}), 201

@user_views.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email y contraseña son obligatorios'}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        # Generar token de acceso
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401