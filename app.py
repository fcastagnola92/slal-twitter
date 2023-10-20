from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from models.models import db
from views.user_views import user_views
from views.task_views import task_views


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:admin@localhost/slas_twitter'
app.config['JWT_SECRET_KEY'] = 'M1$02024'  # Cambia esto con una clave segura y secreta


db.init_app(app)
jwt = JWTManager(app)

# crear bases de datos
with app.app_context():
    db.create_all()


app.register_blueprint(user_views)
app.register_blueprint(task_views)

if __name__ == "__main__":
    app.run(debug=True)