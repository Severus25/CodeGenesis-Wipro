from utils.llm_client import LLMClient
from prompts.agent_prompts import create_documentation_prompt

class DocumentationAgent:
    def __init__(self):
        self.llm_client = LLMClient()

    def generate_docs(self, modernized_code: str, file_path: str) -> str:
        """
        Generates a README.md file for the provided modernized code.
        """
        print(f"  [AGENT_DOCS] Generating documentation for: {file_path}...")
        
        prompt = create_documentation_prompt(modernized_code, file_path)
        
        documentation = self.llm_client.generate(prompt, temperature=0.6)
        print(f"  [AGENT_DOCS] Documentation generation complete for: {file_path}")
        return documentation