from flaskr import create_app


def test_config():
    # test that the app config is set by the arguments
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    # test that the hello view works
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
