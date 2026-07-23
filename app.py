import streamlit as st
import time
import random
from groq import Groq

# 1. Page Configuration (Sabse upar hona chahiye)
st.set_page_config(page_title="CyberMind X", layout="wide")

# 2. Theme Styling
st.markdown("""<style>
    .stApp { background-color: #000000; color: #00ff41; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; }
    .stTextInput>div>div>input { color: #00ff41; }
</style>""", unsafe_allow_html=True)

# 3. API Setup (Secrets ka use karein)
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    client = None # Agar secrets set nahi hain toh error nahi aayega

st.title("⚡ CYBERMIND X - ULTIMATE")

# 4. Sidebar Menu
menu = st.sidebar.radio("CHOOSE MODULE", ["SECURE SCAN", "AI CHATBOT", "SYSTEM BREACH", "CREATIVE LAB", "PREMIUM HUB"])

# 5. Functions
def get_groq_response(user_input):
    if client:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    return "API Key missing! Please configure secrets."

# 6. Main Logic
if menu == "SECURE SCAN":
    st.header("🛡️ THREAT DEFENSE SYSTEM")
    if st.button("RUN DEEP SCAN"):
        st.success("SCAN COMPLETE: NO THREATS FOUND.")

elif menu == "AI CHATBOT":
    st.header("🧠 NEURAL CHATBOT")
    query = st.text_input("Ask CyberMind AI:")
    if st.button("SEND"):
        st.write(get_groq_response(query))

elif menu == "SYSTEM BREACH":
    st.header("💀 SYSTEM BREACH SIMULATOR")
    if st.button("INITIATE BREACH"):
        st.code("[!] BREACHING... [!] ACCESS GRANTED!", language='bash')

elif menu == "CREATIVE LAB":
    st.header("🎨 CREATIVE STUDIO")
    st.write("Generating assets...")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO PRO")
    st.radio("Select Plan:", ["7 Days", "1 Month", "Lifetime"])
    if st.button("ACTIVATE"):
        st.balloons()
