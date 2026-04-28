from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-20250514"

user_question = input("You: ")

message = client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[
        {"role": "user", "content": user_question}
    ]
)

print("Claude: " + message.content[0].text)