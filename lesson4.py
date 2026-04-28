import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
model = "claude-opus-4-5" 
# One growing list of messages
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages):
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return response.content[0].text
messages = []

add_user_message(messages, "Define quantum computing in one sentence.")
answer = chat(messages)
print("Claude:", answer)

add_assistant_message(messages, answer)

add_user_message(messages, "Write another sentence.")
final = chat(messages)
print("Claude:", final)