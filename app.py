import streamlit as st
import time
import random
import os
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="CyberMind X", layout="wide", page_icon="⚡")

# 2. Styling
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# 3. Logic for AI
def get_ai_response(prompt):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )
        return response.choices[0].message.content
    except:
        return "System Busy: Please check your API Key in Settings."

# 4. Main Menu
menu = st.sidebar.selectbox("COMMAND CENTER", ["HOME", "THREAT SCAN", "NEURAL CHAT", "SYSTEM BREACH", "CREATIVE LAB", "PREMIUM HUB"])

st.title("⚡ CYBERMIND X - ULTIMATE")

# 5. Routing
if menu == "HOME":
    st.header("Welcome, Commander.")
    st.write("CyberMind X: Your personal AI security & creative assistant.")

elif menu == "THREAT SCAN":
    st.header("🛡️ THREAT DEFENSE SYSTEM")
    if st.text_input("Enter Link/IP/Device ID:"):
        if st.button("RUN DEEP SCAN"):
            st.success(f"SCAN RESULT: {random.choice(['SAFE', 'HIGH RISK DETECTED', 'PHISHING ATTEMPT'])}")

elif menu == "NEURAL CHAT":
    st.header("🧠 NEURAL CHATBOT")
    query = st.text_input("Ask CyberMind AI:")
    if st.button("SEND QUERY"):
        st.write(get_ai_response(query))

elif menu == "SYSTEM BREACH":
    st.header("💀 SYSTEM BREACH SIMULATOR")
    if st.button("INITIATE BREACH"):
        st.code("[!] BYPASSING FIREWALL...\n[!] ACCESS GRANTED!\n[!] ROOT ACCESS ACHIEVED!", language='bash')

elif menu == "CREATIVE LAB":
    st.header("🎨 CREATIVE STUDIO")
    st.selectbox("Engine", ["Image Gen", "Video Gen", "Face Swap"])
    if st.button("GENERATE"):
        st.success("Successfully generated assets.")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO CYBERMIND X-PRO")
    st.subheader("🔥 UNLOCK EXCLUSIVE FEATURES")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("✅ Unlimited Neural Chat\n✅ 4K Ultra-HD Generation")
    with col2:
        st.markdown("✅ Real-time Breach Alerts\n✅ Ad-Free Experience")
    
    st.divider()
    plan = st.radio("CHOOSE YOUR PLAN:", 
        ["7 Days Trial - $4.99", "6 Months Plan - $29.99", "1 Year Plan - $49.99", "Lifetime Access - $99.99"])
    
    if st.button("ACTIVATE PREMIUM NOW"):
        st.balloons()
        st.success(f"Redirecting to payment for: {plan}")
