# import google.generativeai as genai
# from config import GOOGLE_API_KEY

# class LLMClient:
#     def __init__(self):
#         if not GOOGLE_API_KEY:
#             raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
#         genai.configure(api_key=GOOGLE_API_KEY)
        
#         # FINAL CORRECTION: Using the latest and most robust model name.
#         # This model is guaranteed to be available on the new API version.
#         self.model = genai.GenerativeModel('gemini-2.5-pro')

#     def generate(self, prompt: str, temperature: float = 0.4) -> str:
#         """Generates content using the configured LLM."""
#         try:
#             config = genai.GenerationConfig(temperature=temperature)

#             response = self.model.generate_content(prompt, generation_config=config)
            
#             # Clean up the response to remove markdown formatting if present
#             clean_response = response.text.replace("```python", "").replace("```", "").strip()
#             return clean_response
            
#         except Exception as e:
#             # Provide a more detailed error message for debugging
#             print(f"  [LLM_ERROR] An error occurred while communicating with the Google AI API: {e}")
#             return f"Error: Could not generate response. Details: {e}"



import os
import openai
from dotenv import load_dotenv

# Load environment variables from the .env file in your project root
load_dotenv()

class LLMClient:
    def __init__(self):
        """
        Initializes the LLM client to connect to Azure OpenAI services.
        It securely loads credentials from the .env file.
        """
        try:
            # Load all necessary credentials from the environment variables
            self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
            self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
            self.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

            # Validate that all required variables are present
            if not all([self.api_key, self.endpoint, self.deployment_name, self.api_version]):
                raise ValueError("One or more required Azure OpenAI environment variables are missing.")

            # Configure and initialize the official Azure OpenAI client
            self.client = openai.AzureOpenAI(
                api_key=self.api_key,
                api_version=self.api_version,
                azure_endpoint=self.endpoint
            )
        except Exception as e:
            print(f"  [LLM_ERROR] Failed to initialize the Azure OpenAI client: {e}")
            raise  # Stop the application if the client cannot be initialized

    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        """
        Generates content using the configured Azure OpenAI model (e.g., GPT-4o).
        """
        try:
            # Create the chat completion request for the Azure API
            response = self.client.chat.completions.create(
                model=self.deployment_name,  # This is your 'engine_name'
                messages=[
                    {"role": "system", "content": "You are an expert software engineer specializing in legacy code modernization. You provide only raw code as output, without any explanations, comments about your process, or markdown formatting tags like ```python."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=4096  # A safe limit for generating complete code files
            )

            # === THIS IS THE CORRECTED LINE ===
            # The API returns a list of choices. We need to access the first item
            # before we can get its 'message' and 'content'.
            clean_response = response.choices[0].message.content.strip()
            
            return clean_response

        except Exception as e:
            print(f"  [LLM_ERROR] An error occurred while communicating with the Azure OpenAI API: {e}")
            return f"Error: Could not generate response. Details: {e}"
