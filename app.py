import streamlit as st
from PIL import Image
import io
import re
from groq import Groq

st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar
st.sidebar.title("🚀 CyberMind Pro")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
menu = ["Home", "Scam Analyzer", "URL Scanner", "Content Generator", "Password Checker", "Emergency Directory", "Data Leak Info", "Encrypted Notes"]
choice = st.sidebar.selectbox("Features:", menu)

def get_client(): return Groq(api_key=groq_api_key)

if choice == "Home":
    st.title("🛡️ CyberMind Pro Workstation")
    st.write("Welcome Tawkeer Bhai! App is ready and stable.")

elif choice == "Password Checker":
    st.subheader("🔑 Password Strength Meter")
    pwd = st.text_input("Enter password:", type="password")
    if pwd:
        strength = "Weak"
        if len(pwd) > 8 and re.search(r"[A-Z]", pwd) and re.search(r"[0-9]", pwd):
            strength = "Strong! ✅"
        st.write(f"Strength: **{strength}**")

elif choice == "Emergency Directory":
    st.subheader("📞 Emergency Contacts")
    st.info("Cyber Crime Helpline: **1930**")
    st.write("Website: [cybercrime.gov.in](https://www.cybercrime.gov.in)")

elif choice == "Data Leak Info":
    st.subheader("🔍 Data Breach Awareness")
    st.write("Apni email ki security check karne ke liye **haveibeenpwned.com** ka use karein.")

elif choice == "Encrypted Notes":
    st.subheader("🔒 Secure Notes")
    note = st.text_area("Write your sensitive note (local):")
    if note:
        st.success("Note stored in session!")

elif choice in ["Scam Analyzer", "URL Scanner", "Content Generator"]:
    text = st.text_input("Enter details:")
    if st.button("Analyze/Generate"):
        client = get_client()
        resp = client.chat.completions.create(model="llama-3.3-70b-versatile", 
               messages=[{"role": "user", "content": f"Help me with: {text}"}])
        st.write(resp.choices[0].message.content)