import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

# Import the FastAPI app and Pydantic model from the script to be tested
# Assuming the provided code is in a file named `legacy_user.py`
from legacy_user import User, app, db_users

# --- Test Setup ---

# Create a TestClient instance for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_db_state():
    """
    A pytest fixture that runs automatically before each test.
    It resets the in-memory database to a known initial state,
    ensuring that tests are isolated and don't interfere with each other.
    """
    # Define the pristine, initial state of the database
    original_db = {
        1: User(id=1, name="Alice", email="alice@example.com"),
        2: User(id=2, name="Bob", email="bob@example.com"),
    }
    # Clear the current db and update it with the original state
    db_users.clear()
    db_users.update(original_db)
    # The 'yield' keyword is not strictly necessary here since cleanup happens
    # implicitly by re-running the fixture, but it's good practice for more complex setups.
    yield


# --- 1. Pydantic Model Unit Tests ---

def test_user_model_creation_success():
    """Tests successful creation of a User instance with valid data."""
    user = User(id=100, name="Charlie", email="charlie@example.com")
    assert user.id == 100
    assert user.name == "Charlie"
    assert user.email == "charlie@example.com"
    assert isinstance(user.id, int)
    assert isinstance(user.name, str)

def test_user_model_creation_invalid_email():
    """Tests that creating a User with an invalid email raises a ValidationError."""
    with pytest.raises(ValidationError) as excinfo:
        User(id=101, name="David", email="david-is-not-an-email")
    # Check that the error message contains information about the invalid field
    assert "email" in str(excinfo.value)

def test_user_model_creation_missing_field():
    """Tests that creating a User with a missing required field raises a ValidationError."""
    with pytest.raises(ValidationError) as excinfo:
        User(id=102, name="Eve") # Missing 'email'
    assert "email" in str(excinfo.value)
    assert "field required" in str(excinfo.value)

def test_user_model_creation_incorrect_type():
    """Tests that creating a User with an incorrect data type raises a ValidationError."""
    with pytest.raises(ValidationError) as excinfo:
        User(id="not-an-int", name="Frank", email="frank@example.com")
    assert "id" in str(excinfo.value)
    assert "value is not a valid integer" in str(excinfo.value)


# --- 2. FastAPI Endpoint Unit Tests ---

def test_read_root():
    """Tests the root endpoint to ensure it returns the welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Modernized User API"}

def test_get_user_by_id_success():
    """Tests retrieving an existing user by their ID."""
    response = client.get("/users/1")
    assert response.status_code == 200
    expected_data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
    assert response.json() == expected_data

def test_get_user_by_id_not_found():
    """Tests retrieving a non-existent user, expecting a 404 error."""
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User with id 999 not found"}

def test_create_user_success():
    """Tests successfully creating a new user."""
    new_user_data = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/users/", json=new_user_data)
    
    # Verify the response
    assert response.status_code == 201
    assert response.json() == new_user_data
    
    # Verify that the user was actually added to the in-memory database
    assert 3 in db_users
    assert db_users[3].name == "Charlie"

def test_create_user_already_exists():
    """Tests creating a user with an ID that already exists, expecting a 400 error."""
    existing_user_data = {"id": 1, "name": "Alice V2", "email": "alice.v2@example.com"}
    response = client.post("/users/", json=existing_user_data)
    
    assert response.status_code == 400
    assert response.json() == {"detail": "User with id 1 already exists"}

def test_create_user_invalid_payload():
    """Tests creating a user with an invalid payload (bad email), expecting a 422 error."""
    invalid_user_data = {"id": 4, "name": "David", "email": "invalid-email"}
    response = client.post("/users/", json=invalid_user_data)
    
    # FastAPI/Pydantic automatically returns a 422 Unprocessable Entity for validation errors
    assert response.status_code == 422
    # The response body contains detailed validation error information
    error_detail = response.json()["detail"][0]
    assert error_detail["loc"] == ["body", "email"]
    assert "invalid email address" in error_detail["msg"]

def test_update_user_name_success():
    """Tests successfully updating an existing user's name."""
    new_name = "Alicia"
    response = client.put(f"/users/1?new_name={new_name}")
    
    # Verify the response
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 1
    assert response_data["name"] == new_name
    assert response_data["email"] == "alice@example.com" # Email should be unchanged
    
    # Verify the change in the actual in-memory database
    assert db_users[1].name == new_name

def test_update_user_name_not_found():
    """Tests updating a non-existent user, expecting a 404 error."""
    response = client.put("/users/999?new_name=Ghost")
    assert response.status_code == 404
    assert response.json() == {"detail": "User with id 999 not found"}