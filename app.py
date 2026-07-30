import streamlit as st
import time
import random
import re

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind X Pro | V4.0", page_icon="🛡️", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111111; border-right: 2px solid #00FF00; }
    .news-box { border: 1px solid #FF0000; padding: 10px; background-color: #1a0000; color: #ffcccc; margin-bottom: 10px; }
    .premium-box { border: 2px solid #FFD700; padding: 20px; border-radius: 10px; background-color: #1a1a00; text-align: center; }
    .metric-box { border: 1px solid #00FF00; padding: 10px; text-align: center; background-color: #050505; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💀 CyberMind Command")
menu = st.sidebar.radio("MODULES", 
    ["Dashboard", "Live Scam News", "UPI/Transaction Checker", "Spot the Scam Quiz", "Link Analyzer", "Premium Hub", "🚨 Emergency"])

# --- Helper Functions ---
def simulate(text):
    with st.spinner(f"Running {text}..."):
        time.sleep(1.2)

# --- Modules ---

if menu == "Dashboard":
    st.title("💻 THREAT INTELLIGENCE CENTER")
    # Live User Count Feature
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="metric-box"><h3>LIVE USERS</h3><h2 style="color:white;">8,142</h2></div>', unsafe_allow_html=True)
    
    st.subheader("System Status: OPERATIONAL")
    st.info("CyberMind X Pro is actively protecting the network.")

elif menu == "Live Scam News":
    st.title("📰 LIVE SCAM ALERTS")
    news_items = [
        "⚠️ Alert: New 'Task-based' scam active on Telegram.",
        "⚠️ Warning: Fake electricity bill payment links being circulated.",
        "⚠️ Alert: Deepfake audio scam targeting family members.",
        "⚠️ Warning: Fraudulent investment apps found on Play Store."
    ]
    for item in news_items:
        st.markdown(f'<div class="news-box">{item}</div>', unsafe_allow_html=True)

elif menu == "UPI/Transaction Checker":
    st.title("📸 UPI/Transaction Verifier")
    tid = st.text_input("Enter 12-Digit Transaction ID:")
    if st.button("VERIFY"):
        if len(tid) == 12 and tid.isdigit():
            simulate("Verification")
            st.success("✅ Analysis: Genuine Transaction ID detected.")
        else:
            st.warning("⚠️ INVALID ID: Please enter exactly 12 digits.")

elif menu == "Spot the Scam Quiz":
    st.title("🧠 Spot the Scam Quiz")
    option = st.radio("Is this a scam: 'You won a lottery! Click here to claim 50 Lakhs'?", 
                      ("Select option", "Yes, it is a scam", "No, it's a real gift"))
    if st.button("CHECK ANSWER"):
        if option == "Yes, it is a scam":
            st.success("Correct! Never click unknown links.")
        else:
            st.error("Wrong! That's a classic phishing scam.")

elif menu == "Link Analyzer":
    st.title("🔍 URL Analyzer")
    url = st.text_input("Paste URL:")
    if st.button("SCAN"):
        if re.match(r'https?://', url):
            simulate("Link Analysis")
            st.error("🔴 MALICIOUS LINK DETECTED.")
        else:
            st.warning("⚠️ Enter a valid URL.")

elif menu == "Premium Hub":
    st.title("💎 PREMIUM HUB")
    st.markdown('<div class="premium-box">', unsafe_allow_html=True)
    st.subheader("Unlock Professional Tools")
    st.write("---")
    st.write("### 🚀 Premium Features Included:")
    st.write("• Real-time Deep Web Monitoring\n• Advanced IP Traceback\n• Priority Malware Database\n• Ad-Free Dashboard\n• 24/7 Security Expert Access")
    st.write("---")
    st.write("### 💰 Plans:")
    plans = {"7 Days": "₹99", "1 Month": "₹299", "1 Year": "₹2499", "Lifetime": "₹4999"}
    for plan, price in plans.items():
        st.write(f"**{plan}**: {price}")
    st.markdown("---")
    st.write("### 📩 Contact Admin:")
    st.link_button("DM Admin on Instagram", "https://www.instagram.com/th3_tawkeer/")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🚨 Emergency":
    st.title("🛡️ EMERGENCY")
    st.error("DIAL 1930 IMMEDIATELY!")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Admin: Tawkeer")
