from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict

# --- 1. Modernized Data Model (equivalent to LegacyUser.java) ---
# Pydantic's BaseModel is the modern, Pythonic equivalent of a Java POJO/data class.
# It provides type validation, serialization, and documentation automatically.
# Field names are converted to Python's snake_case convention.
class User(BaseModel):
    """Represents a user in the system."""
    id: int
    name: str
    email: EmailStr

# --- 2. FastAPI Application to Expose the Logic as a RESTful API ---
app = FastAPI(
    title="Modernized User API",
    description="An API to manage users, refactored from a legacy Java class.",
    version="1.0.0"
)

# A simple in-memory dictionary to act as a database for demonstration purposes.
# In a real-world application, this would be a connection to a database
# like PostgreSQL, MySQL, or a NoSQL DB.
db_users: Dict[int, User] = {
    1: User(id=1, name="Alice", email="alice@example.com"),
    2: User(id=2, name="Bob", email="bob@example.com"),
}

# --- 3. API Endpoints (equivalent to class methods/business logic) ---

@app.get("/", tags=["General"])
def read_root():
    """A welcome endpoint for the API."""
    return {"message": "Welcome to the Modernized User API"}

@app.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user_by_id(user_id: int):
    """
    Retrieves a user's information by their ID.
    This replaces the functionality of the Java `get...` methods and `displayUserInfo`.
    """
    user = db_users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user

@app.post("/users/", response_model=User, status_code=201, tags=["Users"])
def create_user(user: User):
    """
    Creates a new user.
    This replaces the functionality of the Java constructor. The request body
    (JSON) is automatically parsed and validated into a User object.
    """
    if user.id in db_users:
        raise HTTPException(status_code=400, detail=f"User with id {user.id} already exists")
    db_users[user.id] = user
    return user

@app.put("/users/{user_id}", response_model=User, tags=["Users"])
def update_user_name(user_id: int, new_name: str):
    """
    Updates a user's name.
    This replaces the functionality of the Java `setUserName` method.
    """
    user = db_users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    
    user.name = new_name
    db_users[user_id] = user
    return user

# To run this application:
# 1. Save the code as a Python file (e.g., `main.py`).
# 2. Install the necessary libraries:
#    pip install fastapi "uvicorn[standard]" pydantic email-validator
# 3. Run the server from your terminal:
#    uvicorn main:app --reload
# 4. Access the interactive API documentation at http://127.0.0.1:8000/docs