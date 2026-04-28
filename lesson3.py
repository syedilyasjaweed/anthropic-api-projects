from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-20250514"

conversation_history = []

print("Chat with Claude! (type 'quit' to exit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=conversation_history
    )
    
    claude_response = message.content[0].text
    
    conversation_history.append({
        "role": "assistant",
        "content": claude_response
    })
    
    print("Claude: " + claude_response)