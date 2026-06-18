from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv(dotenv_path=r"C:\Users\My Computer\Desktop\TheLionYouDontSee\myProject\.env")

# Set OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing!")
openai.api_key = OPENAI_API_KEY


# Test conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! Can you help me with content ideas?"}
]

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=150
    )
    print("Ari's Response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
