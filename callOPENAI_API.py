import os
import openai
import sys
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

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





# response = client.responses.create(
#   model="gpt-4o-mini",
#   input="write about sundhar picai",
#   store=True,
# )

# print(response.output_text)

# write a haiku about ai
# import base64
# from openai import OpenAI

# client = OpenAI()

# img = client.images.generate(
#     model="gpt-image-1",
#     prompt="A cute baby sea otter",
#     n=1,
#     size="1024x1024"
# )

# image_bytes = base64.b64decode(img.data[0].b64_json)
# with open("output.png", "wb") as f:
#     f.write(image_bytes)