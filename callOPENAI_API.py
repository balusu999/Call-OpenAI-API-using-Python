import os
import openai
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
api_key=OPENAI_API_KEY
)

prompt = ""
while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    else:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print("Chatbot:", response.choices[0].message.content)
