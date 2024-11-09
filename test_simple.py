import os
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def test_simple():
    load_dotenv()
    
    # Récupérer et vérifier la clé API
    api_key = os.getenv('MISTRAL_API_KEY')
    print(f"Clé API trouvée: {api_key[:5]}...")
    
    try:
        # Initialiser le client
        client = MistralClient(api_key=api_key)
        
        # Message test avec le bon format
        messages = [
            ChatMessage(
                role="user",
                content="Bonjour!"
            )
        ]
        
        # Appel API
        response = client.chat(
            model="mistral-tiny",
            messages=messages
        )
        
        print("\nRéponse reçue:")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"\nErreur: {str(e)}")
        # Afficher plus de détails sur l'erreur
        import traceback
        print("\nDétails de l'erreur:")
        print(traceback.format_exc())

if __name__ == "__main__":
    print("=== Test Simple Mistral AI ===\n")
    test_simple() 