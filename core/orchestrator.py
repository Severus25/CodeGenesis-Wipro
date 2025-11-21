import os
import sys

# === ROBUST IMPORT FIX START ===
# Get the absolute path of the project's root directory
# This makes the imports work regardless of where you run the script from
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)
# === ROBUST IMPORT FIX END ===

from agents.analysis_agent import CodeModernizationAgent
from agents.testing_agent import TestingAgent
from agents.documentation_agent import DocumentationAgent
from config import LEGACY_CODE_PATH, MODERNIZED_CODE_PATH
from utils.code_parser import get_all_java_files, save_modernized_code

class Orchestrator:
    def __init__(self):
        # Instantiate all our specialized agents
        self.modernization_agent = CodeModernizationAgent()
        self.testing_agent = TestingAgent()
        self.documentation_agent = DocumentationAgent()

    def execute_modernization_pipeline(self):
        """Main pipeline to run the entire multi-agent modernization process."""
        print("--- [ORCHESTRATOR] Starting CodeGenesis Multi-Agent Pipeline ---")

        java_files = get_all_java_files(LEGACY_CODE_PATH)
        if not java_files:
            print("[ORCHESTRATOR] No Java files found. Exiting.")
            return

        print(f"[ORCHESTRATOR] Found {len(java_files)} Java file(s) to process.")

        for file_path in java_files:
            print(f"\n--- Processing file: {os.path.basename(file_path)} ---")

            # === PHASE 1: ANALYSIS & REFACTORING ===
            modernized_code = self.modernization_agent.analyze_and_refactor_file(file_path)
            
            if not modernized_code or modernized_code.startswith("Error:"):
                print(f"[ORCHESTRATOR] Failed to modernize {file_path}. Skipping.")
                continue

            base_name = os.path.basename(file_path)
            file_name_without_ext, _ = os.path.splitext(base_name)
            new_file_name_py = ''.join(['_' + i.lower() if i.isupper() else i for i in file_name_without_ext]).lstrip('_') + '.py'
            output_path_py = os.path.join(MODERNIZED_CODE_PATH, new_file_name_py)
            
            print(f"[ORCHESTRATOR] Saving modernized code to: {output_path_py}")
            save_modernized_code(output_path_py, modernized_code)

            with open(file_path, 'r', encoding='utf-8') as f:
                analysis_context = f.read()

            # === PHASE 2: TEST GENERATION ===
            test_script = self.testing_agent.generate_tests(analysis_context, modernized_code, new_file_name_py)
            if test_script and not test_script.startswith("Error:"):
                test_file_name = 'test_' + new_file_name_py
                output_path_test = os.path.join(MODERNIZED_CODE_PATH, 'tests', test_file_name)
                print(f"[ORCHESTRATOR] Saving generated tests to: {output_path_test}")
                save_modernized_code(output_path_test, test_script)

            # === PHASE 3: DOCUMENTATION GENERATION ===
            documentation = self.documentation_agent.generate_docs(modernized_code, new_file_name_py)
            if documentation and not documentation.startswith("Error:"):
                doc_file_name = 'README_' + file_name_without_ext + '.md'
                output_path_doc = os.path.join(MODERNIZED_CODE_PATH, 'docs', doc_file_name)
                print(f"[ORCHESTRATOR] Saving generated documentation to: {output_path_doc}")
                save_modernized_code(output_path_doc, documentation)

        print("\n--- [ORCHESTRATOR] CodeGenesis Pipeline Finished ---")