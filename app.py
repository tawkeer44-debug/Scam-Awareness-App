import streamlit as st
import time
import random
import re

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind X Pro | ULTIMATE", page_icon="💀", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111111; border-right: 2px solid #00FF00; }
    .news-box { border: 1px solid #FF0000; padding: 10px; background-color: #1a0000; color: #ffcccc; margin-bottom: 10px; }
    .premium-box { border: 2px solid #FFD700; padding: 20px; border-radius: 10px; background-color: #1a1a00; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💀 CyberMind Command")
menu = st.sidebar.radio("MODULES", 
    ["Live Scam News", "UPI/Transaction Checker", "Spot the Scam Quiz", "Link Analyzer", "Premium Plans", "🚨 Emergency"])

# --- Helper Functions ---
def simulate(text):
    with st.spinner(f"Running {text}..."):
        time.sleep(1.5)

# --- Modules ---

# 1. LIVE SCAM NEWS FEED
if menu == "Live Scam News":
    st.title("📰 LIVE SCAM ALERTS")
    news_items = [
        "⚠️ Alert: New 'Task-based' scam active on Telegram.",
        "⚠️ Warning: Fake electricity bill payment links being circulated.",
        "⚠️ Alert: Deepfake audio scam targeting family members reported in NCR.",
        "⚠️ Warning: Fraudulent investment apps found on Play Store."
    ]
    for item in news_items:
        st.markdown(f'<div class="news-box">{item}</div>', unsafe_allow_html=True)
    if st.button("Refresh Feed"): st.rerun()

# 2. UPI/TRANSACTION CHECKER
elif menu == "UPI/Transaction Checker":
    st.title("📸 UPI Transaction Verifier")
    tid = st.text_input("Enter 12-Digit Transaction ID:")
    if st.button("VERIFY"):
        if len(tid) == 12 and tid.isdigit():
            simulate("Verification")
            st.success("✅ Analysis: Genuine Transaction ID detected.")
        else:
            st.warning("⚠️ INVALID ID: Please enter exactly 12 digits.")

# 3. SPOT THE SCAM QUIZ
elif menu == "Spot the Scam Quiz":
    st.title("🧠 Spot the Scam Quiz")
    option = st.radio("Is this a scam: 'You won a lottery! Click here to claim 50 Lakhs'?", 
                      ("Select option", "Yes, it is a scam", "No, it's a real gift"))
    if st.button("CHECK ANSWER"):
        if option == "Yes, it is a scam":
            st.success("Correct! Never click unknown links.")
        else:
            st.error("Wrong! That's a classic phishing scam.")

# OTHER MODULES
elif menu == "Link Analyzer":
    st.title("🔍 URL Analyzer")
    url = st.text_input("Paste URL:")
    if st.button("SCAN"):
        if re.match(r'https?://', url):
            simulate("Link Analysis")
            st.error("🔴 MALICIOUS LINK DETECTED.")
        else:
            st.warning("⚠️ Enter a valid URL.")

elif menu == "Premium Plans":
    st.title("💎 GO PREMIUM")
    st.markdown('<div class="premium-box">', unsafe_allow_html=True)
    st.write("Unlock: Advanced IP Tracking, Deep Web Crawl, 24/7 Support.")
    st.link_button("DM Admin on Instagram", "https://www.instagram.com/tawkeer_official_07/")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🚨 Emergency":
    st.title("🛡️ EMERGENCY")
    st.error("DIAL 1930 IMMEDIATELY!")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Admin: Tawkeer")
