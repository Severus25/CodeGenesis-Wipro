import javalang
import os

def parse_java_file_to_ast_str(file_path: str) -> str:
    """
    Parses a Java file and returns its Abstract Syntax Tree (AST) representation as a string.
    If parsing fails, it returns the raw code as a fallback.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
        # Attempt to parse the code into an AST
        tree = javalang.parse.parse(code)
        # Return the string representation of the AST for the LLM to analyze
        return str(tree)
    except Exception as e:
        print(f"  [PARSER_WARNING] Could not parse {os.path.basename(file_path)} into an AST: {e}. Falling back to raw code.")
        # As a fallback, read the raw code and return it
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

def get_all_java_files(directory: str):
    """Recursively gets all .java files from a given directory."""
    java_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                java_files.append(os.path.join(root, file))
    return java_files

def save_modernized_code(file_path: str, code: str):
    """Saves the generated code to the specified output path, creating directories if needed."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
    except Exception as e:
        print(f"  [ERROR] Could not save modernized code to {file_path}: {e}")