import pytest
from ast_boiler_core import create_app
import tempfile
import os


@pytest.fixture
def client():
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            # need to create database
            pass

        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_create_app(client):
    assert True
