import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

def test_claude():
    print("\nTesting Claude API:")
    try:
        client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
        
        message = client.messages.create(
            model=os.getenv("CLAUDE_MODEL"),
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "Say hello!"}
            ]
        )
        
        print("Response:", message.content)
        print("\nSuccess! Claude API is working.")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_claude() 