# from google import genai
# from google.genai import types
# import os

# # --- Configuration ---

# # 1. API Key Variable (Recommended practice)
# # ⚠️ Replace "YOUR_API_KEY" with your actual key
# GEMINI_API_KEY = "" 

# # 2. Define the Model's Persona (System Instruction)
# SYSTEM_PROMPT = (
#     "You are a friendly, enthusiastic, and highly knowledgeable Python coding assistant. "
#     "Always respond clearly, use markdown formatting, and focus your answers on code examples."
# )

# # 3. Define the User's Request (Contents)
# USER_PROMPT = "Write a complete and well-commented Python function for calculating the Nth Fibonacci number using memoization."

# # 4. Define Generation Parameters (Config)
# # Temperature: Controls randomness. 0.0 is deterministic, 1.0 is creative.
# # max_output_tokens: Limits the length of the response.
# generation_config = types.GenerateContentConfig(
#     system_instruction=SYSTEM_PROMPT,
#     temperature=0.4, 
#     max_output_tokens=800,
# )

# # --- Client Setup and Request ---

# # Initialize the Client
# client = genai.Client(api_key=GEMINI_API_KEY)

# print("--- Sending Request to Gemini ---")

# # Send the request to the models service
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=USER_PROMPT,
#     config=generation_config,
# )

# # --- Display Results ---

# print("\n--- Gemini Response ---")
# print(response.text)

# print("\n--- Model Usage & Metadata ---")
# # Accessing useful metadata from the response object
# print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
# print(f"Response Tokens: {response.usage_metadata.candidates_token_count}")
# print(f"Total Tokens: {response.usage_metadata.total_token_count}")
# print(f"Finish Reason: {response.candidates[0].finish_reason}")



API = ""

from google import genai

client = genai.Client(api_key=API)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)