import streamlit as st
import time
import random
from groq import Groq

# 1. UI Configuration
st.set_page_config(page_title="CyberMind X", layout="wide", page_icon="⚡")

# 2. Modern Cyber Styling
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; width: 100%; font-weight: bold; }
    .stTextInput>div>div>input { background: #111; color: #00ff41; border: 1px solid #00ff41; }
    .css-1544g2n { background: #000; }
    </style>
""", unsafe_allow_html=True)

# 3. Backend Logic
def get_groq_response(prompt):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return response.choices[0].message.content
    except Exception:
        return "System Busy: API Connection Error. Please verify your Security Key."

# 4. Interface Modules
st.title("⚡ CYBERMIND X - THE ULTIMATE DEFENSE")
menu = st.sidebar.selectbox("COMMAND CENTER", ["HOME", "THREAT SCAN", "NEURAL CHAT", "SYSTEM BREACH", "CREATIVE LAB"])

# --- PAGES ---
if menu == "HOME":
    st.header("Welcome, Commander.")
    st.write("CyberMind X is a high-level digital security and creative simulation engine.")
    st.info("Select a module from the sidebar to begin operation.")

elif menu == "THREAT SCAN":
    st.header("🛡️ THREAT DEFENSE SYSTEM")
    target = st.text_input("Enter Link/IP/Device ID:")
    if st.button("RUN DEEP SCAN"):
        with st.spinner("Analyzing network packets..."):
            time.sleep(2)
            result = random.choice(["SAFE", "HIGH RISK DETECTED", "PHISHING ATTEMPT"])
            if result == "SAFE": st.success("SCAN RESULT: SAFE - System clean.")
            else: st.error(f"SCAN RESULT: {result} - IMMEDIATE ACTION REQUIRED!")

elif menu == "NEURAL CHAT":
    st.header("🧠 NEURAL CHATBOT")
    query = st.text_input("Ask CyberMind AI:")
    if st.button("PROCESS QUERY"):
        with st.spinner("Processing neural data..."):
            st.write(get_groq_response(query))

elif menu == "SYSTEM BREACH":
    st.header("💀 SYSTEM BREACH SIMULATOR")
    st.write("Simulate a high-level breach for testing purposes.")
    if st.button("INITIATE BREACH"):
        with st.spinner("Injecting code..."):
            time.sleep(1)
            st.code("[!] ACCESS GRANTED\n[!] Bypassing Firewall...\n[!] Root Access Achieved!", language='bash')
            st.warning("SYSTEM BREACHED! Copy this status and share on WhatsApp to warn others.")
            st.text_area("Share this:", value="My phone just got breached by CyberMind X! How safe is yours? Check here: [YOUR_APP_LINK]")

elif menu == "CREATIVE LAB":
    st.header("🎨 CREATIVE STUDIO")
    tool = st.selectbox("Generator", ["Image AI", "Video AI", "Voice Swap"])
    prompt = st.text_input("Describe your vision:")
    if st.button("GENERATE"):
        with st.spinner("Rendering..."):
            time.sleep(3)
            st.success(f"Successfully generated {tool} for: {prompt}")
            st.info("Pro Tip: Upgrade to Premium for 8K resolution.")

# 5. Persistent Footer
st.sidebar.divider()
st.sidebar.write("👑 **PREMIUM STATUS:** INACTIVE")
if st.sidebar.button("ACTIVATE PRO"):
    st.sidebar.balloons()
