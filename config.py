import os
from dotenv import load_dotenv

load_dotenv()

# Securely load API keys and other configurations
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Project settings
LEGACY_CODE_PATH = "legacy_code_input/sample_java_app/"
MODERNIZED_CODE_PATH = "modernized_code_output/"
TARGET_LANGUAGE = "Python"
TARGET_FRAMEWORK = "FastAPI"