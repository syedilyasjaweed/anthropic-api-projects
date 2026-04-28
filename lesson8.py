import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
model = "claude-opus-4-5"

def add_user_message(messages, content):
    messages.append({"role": "user", "content": content})

def add_assistant_message(messages, content):
    messages.append({"role": "assistant", "content": content})

def chat_streaming(messages, temperature=1.0):
    """Streams response to terminal, returns the full text when done."""
    full_response = ""

    with client.messages.stream(
        model=model,
        max_tokens=1000,
        messages=messages,
        temperature=temperature
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response += text  # build the complete response in parallel

    print()  # newline after streaming ends
    return full_response

# --- Main conversation loop ---
print("Streaming Chat (type 'quit' to exit)\n")
messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    add_user_message(messages, user_input)

    print("Claude: ", end="", flush=True)
    response_text = chat_streaming(messages)

    add_assistant_message(messages, response_text)