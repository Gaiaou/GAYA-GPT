import os
import requests
from dotenv import load_dotenv
from openai import Client
from utils import print_debug

load_dotenv()

def test_env_variables():
    print("\nTesting environment variables:")
    variables = [
        "OPENAI_API_KEY",
        "DEHASHED_API_KEY",
        "DEHASHED_USERNAME",
        "GPT_MODEL_NAME",
        "LEAKOSINT_API_KEY"
    ]
    
    for var in variables:
        value = os.getenv(var)
        if value:
            print(f"{var}: {'*' * len(value)}")  # Hide actual values
        else:
            print(f"{var}: NOT SET")

def test_openai():
    print("\nTesting OpenAI API:")
    try:
        client = Client(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}]
        )
        print("OpenAI API: Working")
    except Exception as e:
        print(f"OpenAI API Error: {str(e)}")

def test_dehashed():
    print("\nTesting Dehashed API:")
    try:
        headers = {'Accept': 'application/json'}
        params = (('query', 'test@example.com'),)
        response = requests.get(
            'https://api.dehashed.com/search',
            headers=headers,
            params=params,
            auth=(os.getenv("DEHASHED_USERNAME"), os.getenv("DEHASHED_API_KEY"))
        )
        if response.status_code == 200:
            print("Dehashed API: Working")
        else:
            print(f"Dehashed API Error: Status code {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Dehashed API Error: {str(e)}")

def test_leakosint():
    print("\nTesting LeakOSINT API:")
    try:
        url = 'https://server.leakosint.com/'
        headers = {'Content-Type': 'application/json'}
        data = {
            'token': os.getenv("LEAKOSINT_API_KEY"),
            'request': 'test@example.com',
            'limit': 100,
            'lang': 'en'
        }
        response = requests.post(url, json=data, headers=headers, verify=False)
        if response.status_code == 200:
            print("LeakOSINT API: Working")
        else:
            print(f"LeakOSINT API Error: Status code {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"LeakOSINT API Error: {str(e)}")

if __name__ == "__main__":
    print("Starting API Tests...")
    test_env_variables()
    test_openai()
    test_dehashed()
    test_leakosint()
    print("\nAPI Tests Complete") 