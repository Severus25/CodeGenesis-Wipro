# CodeGenesis: An Agentic AI Framework for Legacy Code Modernization

## 1. Overview

CodeGenesis is a sophisticated, multi-agent AI framework designed to automate the process of modernizing legacy codebases. It leverages Generative AI and Agentic AI principles to analyze, refactor, test, and document legacy applications, transforming them into modern, cloud-native services.

This project was developed to address the significant challenges of manual code modernization, aiming to drastically reduce timelines, costs, and risks associated with these initiatives.

## 2. Features

-   **Multi-Agent Architecture:** A team of specialized AI agents (Analysis, Refactoring, Testing, Documentation) collaborate for a comprehensive workflow.
-   **Deep Code Analysis:** Uses Abstract Syntax Trees (AST) for a deep structural understanding of the code, not just surface-level text processing.
-   **Automated Refactoring:** Intelligently rewrites legacy Java code into modern Python (FastAPI) applications.
-   **Self-Validation:** An autonomous testing agent generates and runs unit tests to ensure the functional equivalence of the modernized code.
-   **Automated Documentation:** Generates API specifications and project documentation automatically.

## 3. System Architecture

[Insert a diagram of the architecture here for visual appeal]

The system works in a pipeline managed by a central Orchestrator:
1.  **Code Ingestion:** The legacy code is loaded into the system.
2.  **Analysis Phase:** The `CodeAnalysisAgent` parses the code into ASTs and uses an LLM to understand business logic and dependencies.
3.  **Refactoring Phase:** The `RefactoringAgent` uses the analysis to generate new code in the target language and framework.
4.  **Validation Phase:** The `TestingAgent` creates and executes tests against the new code.
5.  **Documentation Phase:** The `DocumentationAgent` generates the final project documentation.

## 4. Technology Stack

-   **Backend:** Python 3.10+
-   **AI/LLM:** Google Gemini API
-   **Frameworks:** LangChain
-   **Code Parsing:** `javalang`, `tree-sitter`
-   **Containerization:** Docker

## 5. Setup and Installation

**Prerequisites:**
-   Python 3.10+
-   Docker
-   A Google AI API Key

**Installation Steps:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/codegenesis.git
    cd codegenesis
    ```

2.  **Create a virtual environment:**
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

## 6. How to Run

1.  Place the legacy Java project you want to modernize into the `legacy_code_input/` directory.
2.  Run the main application:
    ```bash
    python main.py
    ```
3.  Observe the output in the console and find the generated code in the `modernized_code_output/` directory.