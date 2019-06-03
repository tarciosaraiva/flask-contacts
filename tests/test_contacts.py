import os
import tempfile

import pytest

from app import create_app

@pytest.fixture
def app():
    db_path = '/tmp/random'

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path
    })

    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

def test_show_new_contact_form(client):
    response = client.get('/contacts')
    assert 200 == response.status_code

def test_add_contact(client):
    response = client.post('/contacts', data=dict(
        id="abc-1234",
        first_name="John",
        last_name="Doe",
        email="john.doe@gmail.com",
        date_of_birth="1987-10-03"
    ), follow_redirects=True)
    assert 200 == response.status_code

def test_all_contacts(client):
    """list all contacts"""
    response = client.get('/')
    assert 200 == response.status_code
