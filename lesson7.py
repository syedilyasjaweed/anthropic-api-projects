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

def chat(messages, temperature=1.0):          # 1. added temperature parameter
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        temperature=temperature               # 2. passed it to the API
    )
    return response.content[0].text

messages = []
add_user_message(messages, "Give me a movie idea.")

# Low temperature - predictable
answer = chat(messages, temperature=0.0)
print("Low temp:", answer)

add_assistant_message(messages, answer)

# High temperature - creative
add_user_message(messages, "Give me another movie idea.")
answer2 = chat(messages, temperature=1.0)
print("High temp:", answer2)