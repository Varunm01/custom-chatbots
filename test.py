import os
import cohere

API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(API_KEY)

response = co.chat(
    model = 'command-a-03-2025',
    messages = [{'role': 'user', 'content':'Hello world!'}],
)

print(response)
print(response.message.content[0].text)



