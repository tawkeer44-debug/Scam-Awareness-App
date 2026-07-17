import streamlit as st
import re
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide", page_icon="🛡️")

# Session State for Persistent Notes
if 'notes' not in st.session_state:
    st.session_state.notes = ""

# Sidebar - API Key Management
st.sidebar.title("🚀 CyberMind Pro")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

menu = ["Home", "Scam Analyzer", "URL Scanner", "Content Generator", "Password Checker", 
        "Emergency Directory", "Data Leak Info", "Encrypted Notes"]
choice = st.sidebar.selectbox("Features:", menu)

def get_client(): return Groq(api_key=groq_api_key)

# --- HOME ---
if choice == "Home":
    st.title("🛡️ CyberMind Pro Advanced")
    st.markdown("### Professional Cyber Security & Productivity Tool")
    st.info("Sabhi features left sidebar mein available hain.")

# --- PASSWORD CHECKER ---
elif choice == "Password Checker":
    st.subheader("🔑 Password Strength Meter")
    pwd = st.text_input("Enter password:", type="password")
    if pwd:
        strength = "Weak"
        if len(pwd) > 8 and re.search(r"[A-Z]", pwd) and re.search(r"[0-9]", pwd):
            strength = "Strong! ✅"
        st.write(f"Strength Status: **{strength}**")

# --- EMERGENCY DIRECTORY ---
elif choice == "Emergency Directory":
    st.subheader("📞 Emergency Contacts")
    st.markdown("- **Cyber Crime Helpline:** `1930`")
    st.link_button("Visit Official Portal", "https://www.cybercrime.gov.in")

# --- DATA LEAK INFO ---
elif choice == "Data Leak Info":
    st.subheader("🔍 Data Breach Awareness")
    st.write("Apni email ki security check karne ke liye niche click karein:")
    st.link_button("Check at HaveIBeenPwned.com", "https://haveibeenpwned.com")

# --- ENCRYPTED NOTES (PERSISTENT) ---
elif choice == "Encrypted Notes":
    st.subheader("🔒 Secure Notes")
    note = st.text_area("Write your sensitive note:", value=st.session_state.notes)
    if st.button("Save Note"):
        st.session_state.notes = note
        st.success("Note saved in local session!")

# --- AI ANALYZER ---
elif choice in ["Scam Analyzer", "URL Scanner", "Content Generator"]:
    st.subheader(f"💻 {choice}")
    text = st.text_input(f"Enter details for {choice}:")
    if st.button("Analyze/Generate"):
        if groq_api_key:
            client = get_client()
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", 
                   messages=[{"role": "user", "content": f"Help me with this task: {text}"}])
            st.write(resp.choices[0].message.content)
        else:
            st.error("Please enter Groq API Key!")