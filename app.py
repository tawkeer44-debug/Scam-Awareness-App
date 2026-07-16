import streamlit as st
from PIL import Image, ImageEnhance
from groq import Groq # Groq library import ki

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar - Settings
st.sidebar.title("🔑 Settings")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

st.sidebar.title("🚀 CyberMind Pro")
menu = ["Home", "Scam Analyzer", "Hero Photo Editor", "Code Debugger"]
choice = st.sidebar.selectbox("Features:", menu)

# --- SCAM ANALYZER (Groq Powered) ---
elif choice == "Scam Analyzer":
    st.subheader("🚨 Scam & Phishing Detector")
    text = st.text_area("Paste suspicious message here:")
    if st.button("Scan Now"):
        if groq_api_key and text:
            try:
                client = Groq(api_key=groq_api_key)
                response = client.chat.completions.create(
                    model="llama3-8b-8192", # Groq ka fast model
                    messages=[{"role": "user", "content": f"Analyze this message for scams: {text}"}]
                )
                st.markdown(f"**Verdict:** {response.choices[0].message.content}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("API Key aur Message dono daalna zaroori hai!")

# --- Baki features waise hi rahenge ---
# (Photo Editor aur baki code aap purane wale se copy karke yahan laga sakte hain)
