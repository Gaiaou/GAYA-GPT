# GAYA GPT 🌟

<p align="center">
  <img src="assets/gaya_logo.png" alt="GAYA GPT Logo" width="200"/>
</p>

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-purple.svg)
[![GAYA AI](https://img.shields.io/badge/AI-GAYA-magenta.svg)](https://github.com/GAYA-AI)

</div>

GAYA GPT is a sophisticated AI assistant that combines advanced natural language processing with a beautiful cyberpunk interface. Created by GAYA, it represents the future of human-AI interaction in a uniquely aesthetic way.

## ✨ Key Features

- 🤖 Powered by GAYA's Advanced AI System
- 🎨 Custom Cyberpunk Terminal Interface
- 🔮 Quantum-Inspired Response Processing
- 💫 Real-time Neural Animations
- 🌈 Aesthetic ASCII Art Display

## 🚀 Quick Start

1. Clone GAYA:
```bash
git clone https://github.com/GAYA-AI/gaya-gpt.git
cd gaya-gpt
```

2. Set up environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install GAYA's requirements:
```bash
pip install -r requirements.txt
```

4. Configure GAYA:
```env
MISTRAL_API_KEY=your_api_key
```

## 💫 Using GAYA

Launch GAYA:
```bash
python main.py
```

GAYA Commands:
```bash
ask <question>  # Engage with GAYA
clear           # Reset display
exit            # Close GAYA
```

## 🌌 Project Architecture

```
GAYA-GPT/
├── main.py              # GAYA's Core
├── requirements.txt     # Dependencies
├── .env                # Configuration
├── LICENSE             # MIT License
├── README.md           # Documentation
├── assets/            # GAYA's Assets
│   └── gaya_logo.png   # GAYA Logo
└── services/           # GAYA Services
    ├── __init__.py
    └── api_services.py # API Handler
```

## ⚡ Core Dependencies

- colorama (Terminal styling)
- python-dotenv (Environment management)
- mistralai (AI processing)
- requests (API communication)

## 🌟 Contributing to GAYA

We welcome contributions! Here's how to join GAYA's development:

1. Fork GAYA
2. Create your branch (`git checkout -b feature/GAYAEnhancement`)
3. Commit changes (`git commit -m 'Add GAYAEnhancement'`)
4. Push to branch (`git push origin feature/GAYAEnhancement`)
5. Open a Pull Request

## 📜 License

GAYA GPT is released under the MIT License.

## 👑 Creator

- **GAYA** - *Creator & Developer* - [GAYA GitHub](https://github.com/GAYA-AI)

## ⭐ Special Thanks

- The AI Research Community
- Open Source Contributors
- Python Ecosystem Developers

---

<div align="center">
<pre>
 ▄▄ •  ▄▄▄·  ▄· ▄▌ ▄▄▄·     ▄▄ • ▄▄▄▄· ▄▄▄▄▄
▐█ ▀ ▪▐█ ▀█ ▐█▪██▌▐█ ▀█     ▐█ ▀ ▪▐█ ▀█▪•██  
▄█ ▀█▄▄█▀▀█ ▐█▌▐█▪▄█▀▀█     ▄█ ▀█▄▐█▀▀█▄ ▐█.▪
▐█▄▪▐█▐█ ▪▐▌ ▐█▀·.▐█ ▪▐▌    ▐█▄▪▐██▄▪▐█ ▐█▌·
·▀▀▀▀  ▀  ▀   ▀ •  ▀  ▀     ·▀▀▀▀ ·▀▀▀▀  ▀▀▀ 

Created with 💜 by GAYA
</pre>
</div>

## 🔄 AI Provider Configuration

GAYA GPT supports multiple AI providers. You can choose between Mistral AI and OpenAI:

### Using Mistral AI (Default)
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### Using OpenAI (Alternative)
To use OpenAI instead of Mistral AI:

1. Update your `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

2. Modify `services/api_services.py`:
```python
# Comment out Mistral imports
# from mistralai.client import MistralClient
# from mistralai.models.chat_completion import ChatMessage

# Add OpenAI import
from openai import OpenAI

class APIServices:
    def __init__(self):
        # Choose your AI provider
        # self.mistral_key = os.getenv('MISTRAL_API_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=self.openai_key)

    def ai_query(self, prompt):
        try:
            # OpenAI implementation
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": self.hacker_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"[!] System Error: {str(e)}"
```

3. Install OpenAI dependency:
```bash
pip install openai
```

### API Key Information

- **Mistral AI**: Get your API key from [Mistral AI Platform](https://mistral.ai)
- **OpenAI**: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

⚠️ **Important Security Notes**:
- Never share your API keys
- Always use environment variables
- Add `.env` to your `.gitignore`
- Keep your keys secure and rotate them regularly

### Comparing Providers

| Feature | Mistral AI | OpenAI |
|---------|------------|--------|
| Cost | Generally lower | Varies by model |
| Models | Mistral-7B, 8x7B | GPT-3.5, GPT-4 |
| Speed | Fast | Very fast |
| Context | 8K-32K tokens | 4K-128K tokens |
| API Format | Similar to OpenAI | Standard |

Choose the provider that best suits your needs and budget!
