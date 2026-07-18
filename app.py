import streamlit as st
import re
import random
import string
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide", page_icon="🛡️")

# Sidebar
st.sidebar.title("🚀 CyberMind Pro")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

# Menu
menu = ["Home", "Scam Analyzer", "URL Scanner", "Password Generator", "Premium Features"]
choice = st.sidebar.selectbox("Select Feature:", menu)

def get_client(): 
    if groq_api_key:
        return Groq(api_key=groq_api_key)
    return None

# --- PAGES ---

if choice == "Home":
    st.title("🛡️ CyberMind Pro")
    st.write("Main hoon **Peter**, aapka personal Cyber Safety Expert.")
    st.info("Sidebar se feature select karein!")

elif choice == "Scam Analyzer":
    st.subheader("💻 Scam Analyzer")
    text = st.text_input("Kya check karna hai?")
    if st.button("Ask Peter"):
        client = get_client()
        if client:
            resp = client.chat.completions.create(model="llama-3.3-70b-versatile", 
                   messages=[{"role": "user", "content": f"You are Peter, a cyber expert. Help with: {text}"}])
            st.write(f"**Peter:** {resp.choices[0].message.content}")
        else:
            st.error("API Key dalen!")

elif choice == "URL Scanner":
    st.subheader("🌐 URL Scanner")
    url = st.text_input("URL paste karein:")
    if st.button("Scan"):
        st.write("Peter scan kar raha hai... (Beta Version)")

elif choice == "Password Generator":
    st.subheader("🎲 Password Generator")
    length = st.slider("Length:", 8, 20, 12)
    if st.button("Generate"):
        pwd = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
        st.code(pwd)

elif choice == "Premium Features":
    st.title("💎 CyberMind Pro Advanced Suite")
    st.write("Apni security ko professional level par le jayein.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**7 Days**")
        st.subheader("₹49")
        st.link_button("Buy 7 Days", "https://pages.razorpay.com/YOUR_LINK_HERE")

    with col2:
        st.markdown("**Monthly**")
        st.subheader("₹199")
        st.link_button("Buy Monthly", "https://pages.razorpay.com/YOUR_LINK_HERE")

    with col3:
        st.markdown("**Yearly**")
        st.subheader("₹999")
        st.link_button("Buy Yearly", "https://pages.razorpay.com/YOUR_LINK_HERE")

    with col4:
        st.markdown("**Lifetime**")
        st.subheader("₹2499")
        st.link_button("Buy Lifetime", "https://pages.razorpay.com/YOUR_LINK_HERE")
    
    st.info("Sabse safe aur secure payments.")
