from flask import Blueprint, jsonify
from models.user import User

api = Blueprint('api', __name__)

@api.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])
