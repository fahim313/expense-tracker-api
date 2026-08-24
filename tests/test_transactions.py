def get_auth_headers(client):

    # Register user
    client.post(
        "/auth/register",
        json={
            "username": "transactionuser",
            "email": "transactionuser@gmail.com",
            "password": "123456"
        }
    )

    # Login
    response = client.post(
        "/auth/login",
        data={
            "username": "transactionuser",
            "password": "123456"
        }
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


# Create Transaction

def test_create_transaction(client):

    headers = get_auth_headers(client)

    response = client.post(
        "/transactions/",
        json={
            "title": "Grocery Shopping",
            "amount": 1500,
            "type": "expense",
            "category": "Food",
            "date": "2026-08-24"
        },
        headers=headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Grocery Shopping"
    assert data["amount"] == 1500
    assert data["type"] == "expense"
    assert data["category"] == "Food"


# Read All Transactions

def test_get_transactions(client):

    headers = get_auth_headers(client)

    # Create transaction
    client.post(
        "/transactions/",
        json={
            "title": "Lunch",
            "amount": 500,
            "type": "expense",
            "category": "Food",
            "date": "2026-08-24"
        },
        headers=headers
    )

    response = client.get(
        "/transactions/",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 1


# Read One Transaction

def test_get_single_transaction(client):

    headers = get_auth_headers(client)

    create_response = client.post(
        "/transactions/",
        json={
            "title": "Bus Fare",
            "amount": 100,
            "type": "expense",
            "category": "Transport",
            "date": "2026-08-24"
        },
        headers=headers
    )

    transaction_id = create_response.json()["id"]

    response = client.get(
        f"/transactions/{transaction_id}",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == transaction_id
    assert data["title"] == "Bus Fare"


# Filter Transactions

def test_filter_transactions(client):

    headers = get_auth_headers(client)

    client.post(
        "/transactions/",
        json={
            "title": "Grocery Shopping",
            "amount": 1500,
            "type": "expense",
            "category": "Food",
            "date": "2026-08-24"
        },
        headers=headers
    )

    response = client.get(
        "/transactions/filter?type=expense&category=Food",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 1

    for transaction in data:
        assert transaction["type"] == "expense"
        assert transaction["category"] == "Food"


# Update Transaction

def test_update_transaction(client):

    headers = get_auth_headers(client)

    create_response = client.post(
        "/transactions/",
        json={
            "title": "Old Title",
            "amount": 1000,
            "type": "expense",
            "category": "Food",
            "date": "2026-08-24"
        },
        headers=headers
    )

    transaction_id = create_response.json()["id"]

    response = client.put(
        f"/transactions/{transaction_id}",
        json={
            "title": "Updated Title",
            "amount": 2000
        },
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Title"
    assert data["amount"] == 2000


# Delete Transaction

def test_delete_transaction(client):

    headers = get_auth_headers(client)

    create_response = client.post(
        "/transactions/",
        json={
            "title": "Delete Me",
            "amount": 500,
            "type": "expense",
            "category": "Food",
            "date": "2026-08-24"
        },
        headers=headers
    )

    transaction_id = create_response.json()["id"]

    response = client.delete(
        f"/transactions/{transaction_id}",
        headers=headers
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Transaction deleted successfully"