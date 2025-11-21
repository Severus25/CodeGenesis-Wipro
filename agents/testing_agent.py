from utils.llm_client import LLMClient
from prompts.agent_prompts import create_test_generation_prompt

class TestingAgent:
    def __init__(self):
        self.llm_client = LLMClient()

    def generate_tests(self, code_analysis: str, modernized_code: str, file_path: str) -> str:
        """
        Generates pytest unit tests for the provided modernized code.
        """
        print(f"  [AGENT_TEST] Generating tests for: {file_path}...")
        
        prompt = create_test_generation_prompt(code_analysis, modernized_code, file_path)
        
        test_script = self.llm_client.generate(prompt, temperature=0.5)
        print(f"  [AGENT_TEST] Test generation complete for: {file_path}")
        return test_script