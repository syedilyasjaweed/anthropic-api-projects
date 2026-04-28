import anthropic
import json
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
model = "claude-opus-4-5"

def add_user_message(messages, content):
    messages.append({"role": "user", "content": content})

def add_assistant_message(messages, content):
    messages.append({"role": "assistant", "content": content})

def chat(messages, stop_sequences=None):
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        stop_sequences=stop_sequences
    )
    return response.content[0].text

# --- Step 1: See the problem ---
messages = []
add_user_message(messages, "Generate a very short EventBridge rule as JSON")
result = chat(messages)
print("STEP 1:")
print(result)

# --- Step 2: Clean output ---
messages2 = []
add_user_message(messages2, "Generate a very short EventBridge rule as JSON")
add_assistant_message(messages2, "```json")
result2 = chat(messages2, stop_sequences=["```"])
print("STEP 2:")
print(result2)

# --- Step 3: Parse into Python object ---
messages3 = []
add_user_message(messages3, "Generate a very short EventBridge rule as JSON")
add_assistant_message(messages3, "```json")
raw = chat(messages3, stop_sequences=["```"])
clean = json.loads(raw.strip())
print("STEP 3:")
print(type(clean))
print(clean)
  