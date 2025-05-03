# AI-powered-chat-bot-for-mental-health-support
============================================
🧠 AI Mental Health Support Chatbot (Streamlit + GPT)
============================================

This project is a simple, web-based mental health chatbot built using Python, Streamlit, and OpenRouter's GPT-3.5-turbo API. It provides supportive, empathetic conversations to users experiencing emotional distress. The chatbot also includes 10 predefined FAQs to reduce API usage and ensure functionality without internet or a key.

-------------
📁 Project Structure
-------------
- main.py               => Main chatbot code
- README.txt           => Project overview (this file)
- requirements.txt     => Required Python libraries
- .streamlit/secrets.toml (optional) => Securely store API key

-------------
💡 Features
-------------
✅ Empathetic GPT-powered responses using OpenRouter API  
✅ 10 built-in mental health FAQ answers (offline fallback)  
✅ Clean and responsive interface using Streamlit  
✅ Error handling for API failures or missing keys  
✅ Encourages reflection and emotional expression

-------------
⚙️ How to Run
-------------
1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.streamlit/secrets.toml` file (optional):
   [secrets]
   API_KEY = "your_openrouter_api_key"

   OR enter your API key in the app when prompted.

3. Run the chatbot:
   streamlit run main.py

-------------
🧪 Sample Questions (built-in)
-------------
These questions will return instant local answers without calling the API:
- i feel anxious
- i'm feeling depressed
- i can't sleep at night
- i feel alone
- i'm stressed about exams
- i don't feel motivated
- i'm scared about the future
- i feel overwhelmed with work
- i just want someone to talk to
- i'm having a bad day

-------------
🔐 Notes
-------------
- This bot does not store or log user input.
- It is not a substitute for professional mental health care.
- Always ensure user privacy and ethical handling of emotional data.

-------------
📚 References
-------------
Based on current literature and papers, including:
- Anamika Scholar et al. (2024), IJRSCSIT
- Jihyun Lee et al. (2025), JMIR Medical Informatics
- Anna Jørgensen et al. (2024), BMC Mental Health
- And others (see full report or documentation)



