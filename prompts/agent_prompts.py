def create_test_generation_prompt(code_analysis: str, modernized_code: str, file_path: str) -> str:
    """Creates a prompt to generate unit tests for the modernized code."""
    prompt = f"""
    **Objective:** You are a meticulous QA Automation Engineer. Your task is to write a comprehensive suite of unit tests for a Python script using the `pytest` framework.

    **Original Code Analysis:**
    Based on the original Java code, the core logic was determined to be:
    {code_analysis}

    **Modernized Python Code to Test:**
    File: `{file_path}`
    ```python
    {modernized_code}
    ```

    **Instructions:**
    1.  **Analyze:** Based on the original logic and the new Python code, write unit tests that verify the correctness of the modernized code.
    2.  **Framework:** Use the `pytest` framework. Assume `pytest` is installed.
    3.  **Coverage:** Create tests that cover the main functionalities. For a Pydantic model, test object creation and data validation. For an API, test the endpoints.
    4.  **Completeness:** The output must be a single, complete, and runnable Python script containing all necessary imports and test functions.
    5.  **Provide Only Code:** Your final output must be ONLY the complete Python test script. Do not add explanations or markdown tags.

    Begin writing the pytest script now.
    """
    return prompt

def create_documentation_prompt(modernized_code: str, file_path: str) -> str:
    """Creates a prompt to generate a README.md for the modernized code."""
    prompt = f"""
    **Objective:** You are a professional Technical Writer. Your task is to create a clear and concise `README.md` file for a given Python script.

    **Python Script to Document:**
    File: `{file_path}`
    ```python
    {modernized_code}
    ```

    **Instructions:**
    1.  **Analyze:** Read the Python code and understand its purpose. Identify if it's a data model (Pydantic), a web API (FastAPI), or a utility script.
    2.  **Structure:** Create a markdown document with the following sections:
        -   A main title (e.g., `# User Model` or `# Calculator API`).
        -   A brief "Overview" section explaining the script's purpose.
        -   A "Features" or "Attributes" section listing the key components (e.g., class attributes or API endpoints).
        -   A "How to Use" section with a clear code block showing an example of how to use the script (e.g., how to instantiate the class or call the API with `curl`).
    3.  **Clarity:** Use clear language and proper markdown formatting.
    4.  **Provide Only Markdown:** Your output must be ONLY the complete markdown text. Do not add any other explanations.

    Begin writing the README.md file now.
    """
    return prompt