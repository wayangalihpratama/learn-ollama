import ollama
from ollama import Client

ollama.pull("llama3")

client = Client(host="http://localhost:11434")
response = client.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Tell me about Bali?",
        },
    ],
)

print(response["message"]["content"])
