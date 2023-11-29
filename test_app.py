import json
import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_all_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_get_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert 'John' in response.json['name']
    assert 'Doe' in response.json['lastname']

def test_get_user_not_found(client):
    response = client.get('/users/100')
    assert response.status_code == 404

def test_create_user(client):
    data = {'name': 'Jane', 'lastname': 'Smith'}
    response = client.post('/users', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201

def test_create_user_invalid_request(client):
    data = {'name': 'Jane'}
    response = client.post('/users', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400

def test_update_user(client):
    data = {'name': 'Jane'}
    response = client.patch('/users/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 204

def test_update_user_not_found(client):
    data = {'name': 'Jane'}
    response = client.patch('/users/100', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400

def test_create_or_update_user_create(client):
    data = {'name': 'Jane', 'lastname': 'Smith'}
    response = client.put('/users/2', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 204

def test_create_or_update_user_update(client):
    data = {'name': 'Jane'}
    response = client.put('/users/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 204

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204

def test_delete_user_not_found(client):
    response = client.delete('/users/100')
    assert response.status_code == 404

def test_update_user_with_invalid_data(client):
    data = {'invalid_field': 'value'}
    response = client.patch('/users/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400

def test_create_user_missing_data(client):
    data = {'lastname': 'MissingName'}
    response = client.post('/users', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400

def test_create_user_with_same_data(client):
    data = {'name': 'John', 'lastname': 'Doe'}
    response = client.post('/users', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    response = client.post('/users', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201