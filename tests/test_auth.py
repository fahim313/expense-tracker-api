def test_register_user(client):

    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "123456"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "testuser"
    assert data["email"] == "testuser@gmail.com"

    # Password response-
    assert "password" not in data
    assert "hashed_password" not in data


def test_login_user(client):

    # First register
    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "email": "loginuser@gmail.com",
            "password": "123456"
        }
    )

    # Login
    response = client.post(
        "/auth/login",
        data={
            "username": "loginuser",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):

    # Register user
    client.post(
        "/auth/register",
        json={
            "username": "wrongpass",
            "email": "wrongpass@gmail.com",
            "password": "123456"
        }
    )

    # Wrong password
    response = client.post(
        "/auth/login",
        data={
            "username": "wrongpass",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401