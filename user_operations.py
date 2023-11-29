from flask import jsonify, request

users = [{'id': 1, 'name': 'John', 'lastname': 'Doe'}]


def get_all_users_route():
    return get_all_users()


def get_user_by_id_route(user_id):
    return get_user_by_id(user_id)


def create_user_route():
    return create_user()


def update_user_route(user_id):
    return update_user(user_id)


def create_or_update_user_route(user_id):
    return create_or_update_user(user_id)


def delete_user_route(user_id):
    return delete_user(user_id)


def get_all_users():
    return jsonify(users), 200


def get_user_by_id(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404



def create_user():
    data = request.get_json()
    if 'name' in data and 'lastname' in data:
        new_user = {
            'id': len(users) + 1,
            'name': data['name'],
            'lastname': data['lastname']
        }
        users.append(new_user)
        return jsonify({'id': new_user['id']}), 201
    else:
        return jsonify({'error': 'Invalid request'}), 400


def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        if 'name' in data:
            user['name'] = data['name']
        if 'lastname' in data:
            user['lastname'] = data['lastname']
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 400


def create_or_update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    data = request.get_json()
    if user:
        if 'name' in data:
            user['name'] = data['name']
        if 'lastname' in data:
            user['lastname'] = data['lastname']
    else:
        if 'name' in data and 'lastname' in data:
            new_user = {
                'id': user_id,
                'name': data['name'],
                'lastname': data['lastname']
            }
            users.append(new_user)
    return '', 204


def delete_user(user_id):
    global users
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        users = [user for user in users if user['id'] != user_id]
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404

