import streamlit as st
import re
import random
import string
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro Ultra", layout="wide", page_icon="🛡️")

# --- UI Helper ---
if 'notes' not in st.session_state: st.session_state.notes = ""

st.sidebar.title("🚀 CyberMind Pro Ultra")
groq_api_key = st.sidebar.text_input("Groq API Key:", type="password")

# --- MENU NAVIGATION ---
menu = [
    "Home", "Scam Analyzer", "URL Scanner", "Content Generator", 
    "Password Checker", "Password Generator", "Emergency Directory", 
    "Data Leak Info", "Encrypted Notes", "IP Info Tool"
]
choice = st.sidebar.selectbox("Select Feature:", menu)

def get_client(): return Groq(api_key=groq_api_key)

# --- PAGES ---
if choice == "Home":
    st.title("🛡️ Welcome to CyberMind Pro")
    st.write("Aapka All-in-One Cyber Safety Companion.")

elif choice == "Password Checker":
    st.subheader("🔑 Password Strength Meter")
    pwd = st.text_input("Enter password:", type="password")
    if pwd:
        strength = "Weak"
        if len(pwd) > 10 and re.search(r"[A-Z]", pwd) and re.search(r"[0-9]", pwd):
            strength = "Strong! ✅"
        st.write(f"Result: **{strength}**")

elif choice == "Password Generator":
    st.subheader("🎲 Secure Password Generator")
    length = st.slider("Length:", 8, 20, 12)
    if st.button("Generate"):
        chars = string.ascii_letters + string.digits + "!@#$%"
        pwd = ''.join(random.choice(chars) for i in range(length))
        st.code(pwd)

elif choice == "IP Info Tool":
    st.subheader("🌐 IP Lookup (Simulation)")
    ip = st.text_input("Enter IP Address:")
    if st.button("Lookup"):
        st.write(f"Displaying info for: {ip} ... (Direct API integration ready)")

elif choice == "Emergency Directory":
    st.subheader("📞 Emergency Contacts")
    st.markdown("- **Cyber Crime Helpline:** `1930`")
    st.link_button("CyberCrime Portal", "https://www.cybercrime.gov.in")

elif choice == "Data Leak Info":
    st.subheader("🔍 Data Breach Awareness")
    st.link_button("Check at HaveIBeenPwned.com", "https://haveibeenpwned.com")

elif choice == "Encrypted Notes":
    st.subheader("🔒 Secure Notes")
    st.session_state.notes = st.text_area("Write note:", value=st.session_state.notes)
    if st.button("Save"): st.success("Note Saved!")

elif choice in ["Scam Analyzer", "URL Scanner", "Content Generator"]:
    st.subheader(f"💻 {choice}")
    text = st.text_input("Enter details:")
    if st.button("Run AI Analysis"):
        if groq_api_key:
            client = get_client()
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", 
                   messages=[{"role": "user", "content": f"Help with: {text}"}])
            st.write(resp.choices[0].message.content)
        else:
            st.error("Please enter Groq API Key!")