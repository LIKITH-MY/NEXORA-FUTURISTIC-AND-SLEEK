🚀 NEXORA AI Assistant

NEXORA is a powerful AI-powered assistant built with Streamlit that combines multiple productivity and AI tools into a single platform. It provides intelligent chat, PDF analysis, voice assistance, content creation, image generation, weather updates, YouTube search, PowerPoint generation, and more.

✨ Features
💬 AI Chat Assistant
GPT-powered conversational AI
Context-aware responses
Chat history support
📄 PDF Chat
Upload PDF documents
Extract and analyze text
Ask questions about uploaded documents
🎤 Voice Assistant
Speech-to-text input
AI-powered responses
Text-to-speech output
📊 PowerPoint Generator
Generate presentations automatically
Export downloadable PPTX files
🌤️ Weather Forecast
Real-time weather information
Temperature, humidity, and wind details
🎨 AI Image Generator
Generate images using AI
Custom prompt support
📝 Content Creator
Category-based content generation
Blog posts
Business plans
Marketing content
Educational content
Travel guides
Financial reports
🎥 YouTube Search
Search YouTube videos without API keys
View video details and direct links
📋 Audit Trail
Track application activities
Maintain interaction logs
🎮 Snake Game
Built-in classic Snake game
🛠️ Tech Stack
Python
Streamlit
OpenAI GPT
Requests
BeautifulSoup
Pillow (PIL)
PyPDF2
SpeechRecognition
pyttsx3
python-pptx
Pygame
📂 Project Structure
NEXORA/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── modules/
│   ├── chat.py
│   ├── youtube.py
│   ├── weather.py
│   ├── image_gen.py
│   ├── content_creator.py
│   ├── ppt_generator.py
│   ├── voice_assistant.py
│   ├── pdf_chat.py
│   └── snake_game.py
│
├── utils/
│   ├── logger.py
│   └── helpers.py
│
└── data/
    └── audit_log.json
⚙️ Installation
Clone Repository
git clone https://github.com/yourusername/nexora-ai.git
cd nexora-ai
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_openweather_api_key
▶️ Run Application
streamlit run app.py

Application will start at:

http://localhost:8501
🔒 Security Note

Never commit API keys directly into source code.

Use:

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

instead of hardcoding keys.

🎯 Future Enhancements
User Authentication
Database Integration
Multi-language Support
Mobile Responsive UI
AI Agent Automation
Cloud Deployment
Enhanced Analytics Dashboard
👨‍💻 Author

Likith M Y

Artificial Intelligence & Data Science Engineer

📜 License

This project is licensed under the MIT License.
