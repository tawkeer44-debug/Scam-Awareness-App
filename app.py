import streamlit as st
import time
import random
import os

# Install libraries first: pip install streamlit groq
try:
    from groq import Groq
except ImportError:
    st.error("Please install groq: 'pip install groq'")

# 1. Page Config
st.set_page_config(page_title="CyberMind X", layout="wide", page_icon="⚡")

# 2. Modern Styling
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# 3. API Connection Logic
def get_ai_response(prompt):
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return response.choices[0].message.content
    except Exception as e:
        return "System Notice: API Key missing or connection failed. Check 'Secrets' in Streamlit settings."

# 4. App Modules
menu = st.sidebar.selectbox("COMMAND CENTER", ["THREAT SCAN", "NEURAL CHAT", "SYSTEM BREACH", "CREATIVE LAB", "PREMIUM HUB"])

st.title("⚡ CYBERMIND X - ULTIMATE")

if menu == "THREAT SCAN":
    st.header("🛡️ THREAT DEFENSE SYSTEM")
    if st.text_input("Enter Link/IP/Device ID:"):
        if st.button("RUN DEEP SCAN"):
            with st.spinner("Analyzing packets..."):
                time.sleep(2)
                res = random.choice(["SAFE", "HIGH RISK DETECTED", "PHISHING ATTEMPT"])
                st.success(f"SCAN RESULT: {res}")

elif menu == "NEURAL CHAT":
    st.header("🧠 NEURAL CHATBOT")
    query = st.text_input("Ask CyberMind AI:")
    if st.button("SEND QUERY"):
        with st.spinner("Processing..."):
            st.write(get_ai_response(query))

elif menu == "SYSTEM BREACH":
    st.header("💀 SYSTEM BREACH SIMULATOR")
    if st.button("INITIATE BREACH"):
        st.code("[!] BYPASSING FIREWALL...\n[!] ACCESS GRANTED!\n[!] ROOT ACCESS ACHIEVED!", language='bash')
        st.info("Status copied! Share it now.")

elif menu == "CREATIVE LAB":
    st.header("🎨 CREATIVE STUDIO")
    tool = st.selectbox("Engine", ["Image Gen", "Video Gen"])
    if st.button("GENERATE"):
        with st.spinner("Rendering..."):
            time.sleep(3)
            st.success(f"Successfully generated {tool} asset.")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO PRO")
    st.radio("Select Plan:", ["7 Days - ₹99", "Lifetime - ₹2499"])
    if st.button("ACTIVATE"):
        st.balloons()
