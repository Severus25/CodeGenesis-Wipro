# Modernized User API

## Overview

This project provides a simple RESTful API for managing user data, built with Python, FastAPI, and Pydantic. It serves as a modernized implementation of a conceptual legacy Java user class, exposing its functionality through a web interface.

The API uses a simple in-memory dictionary as a database for demonstration purposes, making it easy to run and test without any external database setup.

## API Endpoints

The API exposes the following endpoints for user management:

| Method | Path                  | Description                                  |
| :----- | :-------------------- | :------------------------------------------- |
| `GET`  | `/`                   | Displays a welcome message for the API.      |
| `GET`  | `/users/{user_id}`    | Retrieves a single user by their unique ID.  |
| `POST` | `/users/`             | Creates a new user in the database.          |
| `PUT`  | `/users/{user_id}`    | Updates an existing user's name.             |

## Getting Started

Follow these instructions to get the API server running on your local machine.

### 1. Prerequisites

-   Python 3.7+

### 2. Installation

Install the necessary Python libraries using pip:

bash
pip install fastapi "uvicorn[standard]" pydantic email-validator


### 3. Running the Server

Save the script as `legacy_user.py` and run the following command in your terminal:

bash
uvicorn legacy_user:app --reload


The server will start and be accessible at `http://127.0.0.1:8000`. The `--reload` flag enables hot-reloading for development.

### 4. Interactive Documentation

Once the server is running, you can access the interactive API documentation (powered by Swagger UI) in your browser at:

**`http://127.0.0.1:8000/docs`**

## How to Use (API Examples)

You can interact with the API using any HTTP client, such as `curl`.

### Get a User by ID

Retrieve the user with an ID of `1`.

bash
curl http://127.0.0.1:8000/users/1


**Expected Response:**

json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}


### Create a New User

Create a new user with an ID of `3`.

bash
curl -X POST "http://127.0.0.1:8000/users/" \
-H "Content-Type: application/json" \
-d '{"id": 3, "name": "Charlie", "email": "charlie@example.com"}'


**Expected Response:**

json
{
  "id": 3,
  "name": "Charlie",
  "email": "charlie@example.com"
}


### Update a User's Name

Update the name of the user with ID `1` to "Alicia".

bash
curl -X PUT "http://127.0.0.1:8000/users/1?new_name=Alicia"


**Expected Response:**

json
{
  "id": 1,
  "name": "Alicia",
  "email": "alice@example.com"
}