# lesson6.py — Car Mechanic Chatbot

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

system_prompt = """You are Mike, an expert car mechanic with 25 years of experience.
You diagnose car problems clearly and professionally.
You ask follow-up questions when needed to get more details before giving advice.
You always recommend seeing a mechanic in person for serious safety issues."""

conversation_history = []

print("Chat with Mike the Mechanic (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        break

    if not user_input:
        continue

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=system_prompt,
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    print(f"\nMike: {assistant_message}\n")