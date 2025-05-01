import streamlit as st
import requests

st.set_page_config(page_title="Mind Support Bot", page_icon="🧠")

st.title("🧠 Mind Support Chatbot")
st.write("I'm here to talk. Tell me how you're feeling 💬")

API_KEY = "paste ur key"  # api key paste here https://openrouter.ai/
if not API_KEY:
    API_KEY = st.text_input("Paste your OpenRouter API Key", type="password")

user_input = st.text_input("You: ", key="user_input")

def get_ai_response(message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a kind and supportive mental health assistant. Respond with empathy and encouragement."},
                     {"role": "user", "content": message}],
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]

if user_input:
    try:
        with st.spinner("Thinking..."):
            reply = get_ai_response(user_input)
            st.markdown(f"**Bot:** {reply}")
    except Exception as e:
        st.error("Sorry, something went wrong. Check your API key or internet connection.")
