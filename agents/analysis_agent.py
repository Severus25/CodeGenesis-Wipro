from utils.llm_client import LLMClient
from utils.code_parser import parse_java_file_to_ast_str
from prompts.analysis_prompts import create_analysis_and_refactor_prompt

class CodeModernizationAgent:
    def __init__(self):
        self.llm_client = LLMClient()

    def analyze_and_refactor_file(self, file_path: str) -> str:
        """
        Analyzes a single legacy file and returns the modernized code.
        """
        print(f"  [AGENT] Analyzing and refactoring: {file_path}...")
        
        code_structure = parse_java_file_to_ast_str(file_path)
        
        prompt = create_analysis_and_refactor_prompt(code_structure, file_path)
        
        modernized_code = self.llm_client.generate(prompt)
        print(f"  [AGENT] Refactoring complete for: {file_path}")
        return modernized_code