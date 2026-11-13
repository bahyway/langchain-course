## Get it from : https://ollama.com/dashboard/setup?use=api
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://ollama.com/v1",
    api_key=os.environ["OLLAMA_API_KEY"],
)

completion = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(completion.choices[0].message.content)
