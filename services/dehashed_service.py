import os
import requests
from config import DEHASHED_API_KEY, DEHASHED_EMAIL

class DehashedService:
    def __init__(self):
        self.api_key = DEHASHED_API_KEY
        self.email = DEHASHED_EMAIL
        self.base_url = "https://api.dehashed.com/search"

    def search(self, query):
        try:
            headers = {'Accept': 'application/json'}
            response = requests.get(
                self.base_url,
                auth=(self.email, self.api_key),
                headers=headers,
                params={'query': query}
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)} 