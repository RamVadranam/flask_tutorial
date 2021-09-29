import json

import pytest

from src import main


@pytest.fixture
def app():
    yield main.app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_sum(app, client):
    res = client.get('/total')
    assert res.status_code == 404


def test_add_to_sum_10(app, client):
    res = client.post('/total/20')
    assert res.status_code == 201
    expected = 20
    assert expected == json.loads(res.get_data(as_text=True))


def test_add_to_sum_20(app, client):
    res = client.post('/total/50')
    assert res.status_code == 201
    expected = 70
    assert expected == json.loads(res.get_data(as_text=True))


def test_add_to_sum_404(app, client):
    res = client.post('test/')
    assert res.status_code == 404