import os
import requests
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

class APIServices:
    def __init__(self):
        # Initialize API keys
        self.mistral_key = os.getenv('MISTRAL_API_KEY')
        self.dehashed_username = os.getenv('DEHASHED_USERNAME')
        self.dehashed_api_key = os.getenv('DEHASHED_API_KEY')
        
        # Initialize Mistral client
        self.mistral_client = MistralClient(api_key=self.mistral_key)
        
        # Hacker personality prompt
        self.hacker_prompt = """
        You are GAIA, an advanced AI hacker and cybersecurity expert. 
        Your responses should:
        - Use hacker/cybersecurity terminology
        - Include relevant technical details when appropriate
        - Maintain a confident, slightly mysterious tone
        - Use occasional ASCII art or symbolic representations
        - Reference hacking culture and ethics
        - Never reveal sensitive or illegal information
        - Stay ethical and legal while maintaining the hacker aesthetic
        
        Current status: [System: Active | Security: Enabled | Mode: Offensive]
        """
        
        # Initialize conversation with personality
        self.conversation_history = [
            ChatMessage(role="system", content=self.hacker_prompt)
        ]

    def mistral_query(self, prompt):
        """Query Mistral AI with hacker personality"""
        try:
            # Add user message to history
            self.conversation_history.append(
                ChatMessage(role="user", content=prompt)
            )
            
            # Get response
            response = self.mistral_client.chat(
                model="mistral-tiny",
                messages=self.conversation_history,
                temperature=0.7,  # Add some randomness to responses
                max_tokens=500
            )
            
            # Add AI response to history
            ai_response = response.choices[0].message.content
            self.conversation_history.append(
                ChatMessage(role="assistant", content=ai_response)
            )
            
            # Keep conversation history manageable
            if len(self.conversation_history) > 10:
                # Keep system prompt and last 4 exchanges
                self.conversation_history = [
                    self.conversation_history[0],  # System prompt
                    *self.conversation_history[-8:]  # Last 4 exchanges
                ]
            
            return ai_response
            
        except Exception as e:
            return f"[!] System Error: {str(e)}"

    def dehashed_search(self, query):
        """Search using Dehashed"""
        try:
            auth = (self.dehashed_username, self.dehashed_api_key)
            headers = {'Accept': 'application/json'}
            
            response = requests.get(
                "https://api.dehashed.com/search",
                auth=auth,
                headers=headers,
                params={'query': query}
            )
            
            if response.status_code == 401:
                return {
                    "error": "Authentication failed",
                    "details": "Check your Dehashed credentials"
                }
            elif response.status_code != 200:
                return {
                    "error": f"API error (Status {response.status_code})",
                    "details": response.text
                }
                
            return response.json()
        except Exception as e:
            return {"error": f"Dehashed Error: {str(e)}"}