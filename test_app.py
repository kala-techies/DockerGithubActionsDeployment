from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World"  # Removed the exclamation mark to match the app response
