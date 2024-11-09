import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_dehashed_credentials():
    # First, check if credentials exist
    username = os.getenv("DEHASHED_USERNAME")
    api_key = os.getenv("DEHASHED_API_KEY")
    
    print("\nChecking Dehashed credentials:")
    print(f"Username present: {'Yes' if username else 'No'}")
    print(f"API Key present: {'Yes' if api_key else 'No'}")
    
    if not username or not api_key:
        print("ERROR: Missing credentials in .env file")
        return

    # Test the API
    print("\nTesting Dehashed API connection:")
    headers = {'Accept': 'application/json'}
    params = (('query', 'test@example.com'),)
    
    try:
        response = requests.get(
            'https://api.dehashed.com/search',
            headers=headers,
            params=params,
            auth=(username, api_key)
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...")  # Show first 200 characters
        
        if response.status_code == 200:
            print("\nSuccess! Dehashed API is working correctly.")
        elif response.status_code == 401:
            print("\nError: Invalid credentials. Please check your username and API key.")
        else:
            print(f"\nError: Unexpected response code {response.status_code}")
            
    except Exception as e:
        print(f"Error connecting to Dehashed: {str(e)}")

if __name__ == "__main__":
    print("=== Dehashed API Test ===")
    test_dehashed_credentials() 