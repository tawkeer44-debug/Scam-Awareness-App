# Yeh code ensure karega ki app dono keys ko Secrets se utha rahi hai
openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
eleven_client = ElevenLabs(api_key=st.secrets["ELEVENLABS_API_KEY"])
import streamlit as st
from openai import OpenAI
from gtts import gTTS
import os

# Page Config
st.set_page_config(page_title="CyberMind AI Pro", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("🛡️ CyberMind AI")
    option = st.radio("Features", [
        "🎨 Image Generator", 
        "🗣️ Kashmiri AI Voice", 
        "🔍 Scam Analyzer", 
        "💻 Code Debugger"
    ])

# API Key handling (Streamlit Secrets se)
def get_client():
    try:
        return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    except:
        st.error("Secrets mein API Key set nahi hai!")
        return None

# Features
if option == "🎨 Image Generator":
    st.header("🎨 AI Image Generator")
    prompt = st.text_input("Describe your image:")
    if st.button("Generate"):
        client = get_client()
        if client:
            res = client.images.generate(prompt=prompt, n=1, size="1024x1024")
            st.image(res.data[0].url)

elif option == "🗣️ Kashmiri AI Voice":
    st.header("🗣️ Kashmiri Text-to-Speech")
    text = st.text_area("Kashmiri mein likhein (ya English mein):")
    if st.button("Speak"):
        # gTTS filhal Kashmiri accent ke liye simple TTS use karta hai
        tts = gTTS(text=text, lang='en') 
        tts.save("voice.mp3")
        st.audio("voice.mp3")

elif option == "🔍 Scam Analyzer":
    st.header("🔍 Scam Scanner")
    msg = st.text_area("Paste link or message:")
    if st.button("Analyze"):
        st.warning("Scanning for phishing...")
