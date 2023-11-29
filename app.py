from flask import Flask
from user_operations import get_all_users_route, get_user_by_id_route, create_user_route, update_user_route, create_or_update_user_route, delete_user_route

app = Flask(__name__)

app.add_url_rule('/users', 'get_all_users_route', get_all_users_route, methods=['GET'])
app.add_url_rule('/users/<int:user_id>', 'get_user_by_id_route', get_user_by_id_route, methods=['GET'])
app.add_url_rule('/users', 'create_user_route', create_user_route, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', 'update_user_route', update_user_route, methods=['PATCH'])
app.add_url_rule('/users/<int:user_id>', 'create_or_update_user_route', create_or_update_user_route, methods=['PUT'])
app.add_url_rule('/users/<int:user_id>', 'delete_user_route', delete_user_route, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
