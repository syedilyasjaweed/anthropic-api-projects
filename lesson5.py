# lesson5.py — System Prompts
# A system prompt gives Claude a role or set of rules before the conversation starts.

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

# This is the system prompt — Claude's role/personality for the whole conversation
system_prompt = """You are a helpful and professional assistant.
Answer questions clearly and concisely.""" 

conversation_history = []

print("Chat with Assistant (type 'quit' to exit)\n")

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
        system=system_prompt,          # <-- the new part
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    print(f"\nAssistant: {assistant_message}\n")
   