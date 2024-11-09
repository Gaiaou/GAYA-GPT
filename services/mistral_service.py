from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from config import MISTRAL_API_KEY, MISTRAL_MODEL, MAX_TOKENS, TEMPERATURE

class MistralService:
    def __init__(self):
        self.client = MistralClient(api_key=MISTRAL_API_KEY)
        self.conversation_history = []

    def add_message(self, role, content):
        self.conversation_history.append(
            ChatMessage(role=role, content=content)
        )

    def get_response(self, prompt):
        try:
            # Add user message to history
            self.add_message("user", prompt)

            # Get response from Mistral
            response = self.client.chat(
                model=MISTRAL_MODEL,
                messages=self.conversation_history,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )

            # Extract and add assistant response to history
            assistant_message = response.choices[0].message.content
            self.add_message("assistant", assistant_message)

            return assistant_message

        except Exception as e:
            print(f"Error in Mistral API call: {str(e)}")
            return f"Error: {str(e)}"

    def clear_history(self):
        self.conversation_history = [] 