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

def test_all_contacts(client):
    """list all contacts"""
    rv = client.get('/')
    assert 200 == rv.status_code
