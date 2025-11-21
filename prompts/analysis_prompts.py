from config import TARGET_LANGUAGE, TARGET_FRAMEWORK

def create_analysis_and_refactor_prompt(code_structure: str, file_path: str) -> str:
    """
    Creates a detailed prompt for both analyzing and refactoring the code.
    This single, powerful prompt instructs the model to perform the full task.
    """
    prompt = f"""
    **Objective:** You are an expert software engineer specializing in legacy code modernization. Your task is to analyze a piece of legacy Java code and refactor it into a modern {TARGET_LANGUAGE} application using the {TARGET_FRAMEWORK} framework.

    **Source Java File:** `{file_path}`

    **Analysis of the Code Structure (AST or Raw Code):**
    ```
    {code_structure}
    ```

    **Instructions:**
    1.  **Analyze:** First, deeply understand the purpose of the Java code provided. Identify the main classes, methods, attributes, and the core business logic it represents. What is its primary function?
    2.  **Modernize:** Rewrite this logic as a complete, runnable {TARGET_LANGUAGE} file.
    3.  **Apply Best Practices:**
        -   Use the {TARGET_FRAMEWORK} framework to expose the logic as a RESTful API if applicable. For a data class, create a Pydantic model.
        -   Use modern language features, proper typing, and clear variable names.
        -   Ensure the code is clean, efficient, and follows PEP 8 standards for Python.
    4.  **Provide Only Code:** Your final output should be ONLY the complete, runnable {TARGET_LANGUAGE} code for a single file. Do not include explanations, comments about the process, or markdown formatting tags like ```python. Just the code itself.

    **Example for a Java User Class:** If the Java code defines a User with a name and email, you should generate a Pydantic model in Python.
    
    **Example for a Java Calculator Class:** If the Java code defines a Calculator with add and subtract methods, you should generate a FastAPI application with `/add` and `/subtract` endpoints.

    Begin the refactoring now.
    """
    return prompt