import streamlit as st
import re
import random
import string
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro | Stay Safe", layout="wide", page_icon="🛡️")

# Sidebar
st.sidebar.title("🚀 CyberMind Pro")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

# --- VIRAL SHARE BUTTON ---
st.sidebar.markdown("---")
st.sidebar.subheader("📢 Share this app:")
st.sidebar.write("Apne doston ko fraud se bachayein!")
if st.sidebar.button("Copy App Link 🔗"):
    st.sidebar.code("https://fqbhgvdywmjsdzgg82jfr3.streamlit.app/")
    st.sidebar.success("Link copied! Share it on WhatsApp.")

menu = [
    "Home", "Scam Analyzer", "URL Scanner", "Content Generator", 
    "Password Checker", "Password Generator", "Emergency Directory", 
    "Data Leak Info", "Encrypted Notes"
]
choice = st.sidebar.selectbox("Select Feature:", menu)

def get_client(): return Groq(api_key=groq_api_key)

# --- APP PAGES ---
if choice == "Home":
    st.title("🛡️ CyberMind Pro")
    st.subheader("Bhai, har fraud se bacho!")
    st.markdown("""
    **Is app ke features:**
    - ✅ **Scam Analyzer:** Scammers ko pehchano.
    - ✅ **Password Security:** Secure password banao.
    - ✅ **Emergency Help:** Cyber crime helpline 1930.
    """)
    st.info("Apne doston ke saath share karna na bhoolein!")

# ... (baaki features wahi purane wale hain) ...

elif choice == "Password Generator":
    st.subheader("🎲 Secure Password Generator")
    length = st.slider("Select Length:", 8, 20, 12)
    if st.button("Generate Secure Password"):
        chars = string.ascii_letters + string.digits + "!@#$%"
        pwd = ''.join(random.choice(chars) for i in range(length))
        st.code(pwd)
        st.success("Ye password use karein!")

# ... (Baki logic wahi rahegi) ...