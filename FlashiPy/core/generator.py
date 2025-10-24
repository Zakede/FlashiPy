from google import genai
from google.genai import types

class Generator:
    def __init__(self, api_key: str):
        # Make sure the client is initialized immediately
        self.client = genai.Client(api_key=api_key)

    def generate_card(self, language: str, level: str = "N5", topic: str = "vocab") -> str:
        prompt = f"""
        Generate a flashcard in {language} for level {level} on the topic '{topic}'.

        Output format EXACTLY like this (no extra text, use proper romanization for non-Latin scripts):

        Word: <the word in {language} script or original form>
        Reading: <phonetic reading or romanization>
        Meaning: <English translation>
        Example: <Sentence in {language} with romanization and English translation>"""

        try:
            # Simple call like your working example
            response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            
            # You can add config if you want
            
            # config=types.GenerateContentConfig(
            # safety_settings=[
            #     types.SafetySetting(
            #         category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            #         threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            #     ),])
            
            )

            if response and hasattr(response, 'text') and response.text:
                return response.text.strip()
            else:
                return "Error: Gemini returned no output."

        except Exception as e:
            return f"Error calling Gemini API: {e}"
