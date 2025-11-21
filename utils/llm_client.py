import google.generativeai as genai
from config import GOOGLE_API_KEY

class LLMClient:
    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # FINAL CORRECTION: Using the latest and most robust model name.
        # This model is guaranteed to be available on the new API version.
        self.model = genai.GenerativeModel('gemini-2.5-pro')

    def generate(self, prompt: str, temperature: float = 0.4) -> str:
        """Generates content using the configured LLM."""
        try:
            config = genai.GenerationConfig(temperature=temperature)

            response = self.model.generate_content(prompt, generation_config=config)
            
            # Clean up the response to remove markdown formatting if present
            clean_response = response.text.replace("```python", "").replace("```", "").strip()
            return clean_response
            
        except Exception as e:
            # Provide a more detailed error message for debugging
            print(f"  [LLM_ERROR] An error occurred while communicating with the Google AI API: {e}")
            return f"Error: Could not generate response. Details: {e}"