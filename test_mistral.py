import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import json

def test_mistral():
    print("\nTesting Mistral AI API:")
    
    try:
        # Load environment variables
        load_dotenv()
        
        # Get API key
        api_key = os.getenv('MISTRAL_API_KEY')
        if not api_key:
            print("Error: No API key found in .env file")
            return
            
        print(f"API Key found: {api_key[:5]}...")
        
        # Initialize client
        client = MistralClient(api_key=api_key)

        # Create the message
        message = {
            "role": "user",
            "content": "What is the capital of France?"
        }

        # Make API call
        response = client.chat(
            model="mistral-tiny",
            messages=[message]
        )

        # Print response
        if response and hasattr(response, 'choices') and response.choices:
            print("\nResponse received:")
            print(response.choices[0].message.content)
        else:
            print("\nUnexpected response format:", response)

    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        print("\nFull traceback:")
        print(traceback.format_exc())

if __name__ == "__main__":
    print("=== Mistral AI Test ===")
    test_mistral() 