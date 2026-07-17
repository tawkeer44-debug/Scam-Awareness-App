import streamlit as st
import re
import random
import string
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro | Peter AI", layout="wide", page_icon="🛡️")

# Sidebar
st.sidebar.title("🚀 CyberMind Pro")
st.sidebar.markdown("---")
st.sidebar.subheader("👋 Meet your Assistant: Peter")
st.sidebar.write("Peter yahan aapki safety ke liye hai!")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

# Share Feature
if st.sidebar.button("Copy App Link 🔗"):
    st.sidebar.code("https://fqbhgvdywmjsdzgg82jfr3.streamlit.app/")
    st.sidebar.success("Link copied! Share karo!")

# Menu
menu = [
    "Home", "Scam Analyzer", "URL Scanner", "Content Generator", 
    "Password Checker", "Password Generator", "Emergency Directory", 
    "Data Leak Info", "Encrypted Notes", "IP Info Tool", "Cyber News"
]
choice = st.sidebar.selectbox("Select Feature:", menu)

def get_client(): return Groq(api_key=groq_api_key)

# --- HOME ---
if choice == "Home":
    st.title("🛡️ CyberMind Pro")
    st.write("Hello! Main hoon **Peter**, aapka personal Cyber Safety Expert.")
    st.info("Sidebar se feature select karein aur main aapki turant madad karunga!")

# --- FEATURES ---

elif choice == "Password Generator":
    st.subheader("🎲 Secure Password Generator")
    length = st.slider("Select Length:", 8, 20, 12)
    if st.button("Generate Secure Password"):
        chars = string.ascii_letters + string.digits + "!@#$%"
        pwd = ''.join(random.choice(chars) for i in range(length))
        st.code(pwd)
        st.success("Ye password use karein!")

elif choice == "IP Info Tool":
    st.subheader("🌐 IP Lookup")
    ip = st.text_input("Enter IP Address:")
    if st.button("Lookup"):
        st.write(f"Peter processing IP: {ip}...")
        st.warning("Feature under construction! Peter jald hi IP details laayega.")

elif choice == "Cyber News":
    st.subheader("📰 Recent Cyber News")
    st.write("Peter aapko latest scams ke baare mein update rakhega.")
    st.success("Stay tuned for real-time scam alerts!")

elif choice == "Emergency Directory":
    st.subheader("📞 Emergency Contacts")
    st.markdown("- **Cyber Crime Helpline:** `1930`")
    st.link_button("CyberCrime Portal", "https://www.cybercrime.gov.in")

elif choice == "Data Leak Info":
    st.subheader("🔍 Data Breach Awareness")
    st.link_button("Check at HaveIBeenPwned.com", "https://haveibeenpwned.com")

elif choice == "Encrypted Notes":
    st.subheader("🔒 Secure Notes")
    st.session_state.notes = st.text_area("Write note:", value=st.session_state.get('notes', ''))
    if st.button("Save"): st.success("Note Saved!")

elif choice in ["Scam Analyzer", "URL Scanner", "Content Generator"]:
    st.subheader(f"💻 {choice}")
    text = st.text_input(f"Peter ko batao: {choice} ke liye...")
    
    if st.button("Ask Peter"):
        if groq_api_key:
            client = get_client()
            prompt = f"You are Peter, a professional cyber security expert. Help the user with: {text}"
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", 
                   messages=[{"role": "user", "content": prompt}])
            st.write(f"**Peter:** {resp.choices[0].message.content}")
        else:
            st.error("Peter ko kaam karne ke liye Groq API Key chahiye!")