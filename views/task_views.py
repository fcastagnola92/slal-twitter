from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.models import db, ConversionTask as Task

task_views = Blueprint('task_views', __name__)

@task_views.route('/tasks', methods=['GET'])
@jwt_required()
def tasks():
    # Obtener el ID del usuario actual
    current_user_id = get_jwt_identity()

    # Consultar las tareas de conversión del usuario actual
    tasks = Task.query.filter_by(user_id=current_user_id).all()

    # Formatear los datos para la respuesta
    task_list = [{'task_id': task.id, 'filename': task.original_filename, 'original_extension': task.original_extension,
                  'destination_extension': task.destination_extension, 'available': task.status} for task in tasks]

    return jsonify(task_list), 200
