from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.models import db
from views.user_views import user_views


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:admin@localhost/slas_twitter'

db.init_app(app)
# crear bases de datos
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return 'Hola mundo'

app.register_blueprint(user_views)

if __name__ == "__main__":
    app.run(debug=True)