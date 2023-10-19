from flask import Blueprint, request, jsonify

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
