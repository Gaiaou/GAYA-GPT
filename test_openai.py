import os
from dotenv import load_dotenv
from openai import Client

load_dotenv()

def test_openai_credentials():
    # Check if API key exists
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("GPT_MODEL_NAME")
    
    print("\nChecking OpenAI credentials:")
    print(f"API Key present: {'Yes' if api_key else 'No'}")
    print(f"Model name: {model_name}")
    
    if not api_key:
        print("ERROR: Missing OpenAI API key in .env file")
        return

    # Test the API
    print("\nTesting OpenAI API connection:")
    try:
        client = Client(api_key=api_key)
        
        # Try a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using this model for testing
            messages=[
                {"role": "user", "content": "Say 'Hello, testing OpenAI API!'"}
            ]
        )
        
        print("\nAPI Response:")
        print(response.choices[0].message.content)
        print("\nSuccess! OpenAI API is working correctly.")
        
    except Exception as e:
        print(f"\nError connecting to OpenAI: {str(e)}")
        print("\nCommon solutions:")
        print("1. Check if your API key is valid")
        print("2. Verify you have credits/billing set up at platform.openai.com")
        print("3. Make sure your account is in good standing")

if __name__ == "__main__":
    print("=== OpenAI API Test ===")
    test_openai_credentials()
