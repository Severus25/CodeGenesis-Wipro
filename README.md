# CodeGenesis: An Agentic AI Framework for Legacy Code Modernization

## 1. Overview

CodeGenesis is a sophisticated, multi-agent AI framework designed to automate the entire lifecycle of modernizing legacy applications. It ingests legacy Java code and intelligently transforms it into a production-ready, modern Python service with a complete suite of tests and documentation.

This project moves beyond simple code translation by employing a team of specialized AI agents that collaborate to analyze, refactor, validate, and document the code, drastically reducing the time, cost, and risk associated with application modernization.

## 2. Features

-   **Multi-Agent Architecture:** A pipeline of intelligent agents, each with a specific role:
    -   **Modernization Agent:** Analyzes legacy Java code (using ASTs) and performs an architectural refactoring into a modern Python FastAPI service.
    -   **Testing Agent:** Validates the new code by autonomously writing a comprehensive `pytest` unit test suite.
    -   **Documentation Agent:** Generates clear, professional `README.md` documentation for the new service.
-   **Production-Ready Output:** The final output is not just code, but a complete, runnable, and verifiable project package, including the modernized service, its test suite, and its documentation.
-   **Intelligent Refactoring:** Understands programming concepts and re-architects solutions using modern best practices (e.g., REST APIs, Pydantic data validation).
-   **Containerized & Reproducible:** Includes a `Dockerfile` to ensure the project runs identically in any environment.

## 3. Technology Stack

-   **Backend:** Python 3.10+
-   **AI Engine:** Google Gemini 2.5 Pro
-   **Core AI Framework:** `google-generativeai`
-   **Code Parsing:** `javalang`
-   **Modernized Output Stack:** FastAPI, Pydantic, Uvicorn, Pytest
-   **Containerization:** Docker

## 4. Setup and Installation

**Prerequisites:**
-   Python 3.10+
-   Docker (Optional, see Docker section)
-   A Google AI API Key

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/codegenesis.git
    cd codegenesis
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    -   Create a file named `.env` in the root directory.
    -   Add your API key to this file:
        ```
        GOOGLE_API_KEY="your_google_api_key_here"
        ```

## 5. How to Run the Modernization Pipeline

1.  Place the legacy Java project you want to modernize into the `legacy_code_input/` directory.
2.  Run the main application from the project's root directory:
    ```bash
    python main.py
    ```
3.  The complete, modernized project (Python code, tests, and docs) will be generated in the `modernized_code_output/` directory.

## 6. How to Run the Generated API

After the pipeline has successfully run, you can launch the newly created web service.

1.  **Install FastAPI/Uvicorn:**
    ```bash
    pip install "fastapi[all]"
    ```
2.  **Navigate to the output directory:**
    ```bash
    cd modernized_code_output
    ```
3.  **Launch the server:** (Assuming the generated file is `legacy_user.py`)
    ```bash
    uvicorn legacy_user:app --reload
    ```
4.  **Access the interactive documentation:** Open your browser and go to **`http://127.0.0.1:8000/docs`**.

## 7. How to Use Docker

This project includes a `Dockerfile` to build a self-contained image of the CodeGenesis application.

1.  **Build the Docker image:**
    From the project's root directory, run:
    ```bash
    docker build -t codegenesis-app .
    ```

2.  **Run the Docker container:**
    This command runs the modernization pipeline inside the container.
    ```bash
    docker run --rm -v ./modernized_code_output:/app/modernized_code_output -v ./legacy_code_input:/app/legacy_code_input --env-file .env codegenesis-app
    ```
    - `--rm`: Deletes the container after it finishes.
    - `-v`: Mounts your local output/input directories into the container so it can read the legacy code and save the new code to your machine.
    - `--env-file .env`: Securely passes your API key to the container.
