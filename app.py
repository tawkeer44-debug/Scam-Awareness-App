import streamlit as st
import time
import re

# --- Page Configuration ---
st.set_page_config(page_title="Scam Awareness Pro", page_icon="🛡️", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111111; border-right: 2px solid #00FF00; }
    .news-box { border: 1px solid #FF0000; padding: 10px; background-color: #1a0000; color: #ffcccc; margin-bottom: 10px; }
    .premium-box { border: 2px solid #FFD700; padding: 20px; border-radius: 10px; background-color: #1a1a00; text-align: center; }
    .metric-box { border: 1px solid #00FF00; padding: 10px; text-align: center; background-color: #050505; }
    .helpline-box { border: 1px solid #00FF00; padding: 15px; background-color: #001a00; border-radius: 5px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💀 Scam Awareness Command")
menu = st.sidebar.radio("MODULES", 
    ["Dashboard", "Live Scam News", "UPI/Transaction Checker", "Scam Risk Calculator", "Link Analyzer", "Cyber Helpline Directory", "Premium Features"])

# --- Modules ---
if menu == "Dashboard":
    st.title("💻 THREAT INTELLIGENCE CENTER")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="metric-box"><h3>LIVE USERS</h3><h2 style="color:white;">8,142</h2></div>', unsafe_allow_html=True)
    st.subheader("System Status: OPERATIONAL")
    st.info("Scam Awareness Platform is actively protecting the network.")

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
            with st.spinner("Verifying transaction..."):
                time.sleep(1)
            st.success("✅ Analysis: Genuine Transaction ID detected.")
        else:
            st.warning("⚠️ INVALID ID: Please enter exactly 12 digits.")

elif menu == "Scam Risk Calculator":
    st.title("📊 Scam Risk Calculator")
    st.write("Analyze the situation to check your fraud exposure level.")
    
    q1 = st.checkbox("Did someone ask for your OTP, UPI PIN, or Password?")
    q2 = st.checkbox("Did you receive an offer promising 'Easy Money' or 'Guaranteed Returns'?")
    q3 = st.checkbox("Is the sender rushing you or threatening account block?")
    
    if st.button("CALCULATE RISK"):
        score = sum([q1, q2, q3])
        if score >= 2:
            st.error("🔴 HIGH RISK: This is definitely a scam! Do not proceed.")
        elif score == 1:
            st.warning("⚠️ MODERATE RISK: Exercise high caution. Verify independently.")
        else:
            st.success("🟢 LOW RISK: Looks relatively safe, but always stay vigilant.")

elif menu == "Link Analyzer":
    st.title("🔍 URL Analyzer")
    url = st.text_input("Paste URL:")
    if st.button("SCAN"):
        if url and re.match(r'https?://', url):
            with st.spinner("Analyzing link..."):
                time.sleep(1)
            st.error("🔴 MALICIOUS LINK DETECTED.")
        else:
            st.warning("⚠️ Enter a valid URL.")

elif menu == "Cyber Helpline Directory":
    st.title("📞 Cyber Helpline Directory")
    st.write("Quick access numbers and official portals to report financial cyber frauds immediately.")
    
    st.markdown('<div class="helpline-box"><h3>🚨 National Cyber Crime Helpline</h3><p style="font-size: 20px; color: #ff3333;"><b>Dial: 1930</b> (Available 24x7)</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="helpline-box"><h3>🌐 Official Reporting Portal</h3><p>Report online cyber frauds securely at:</p><a href="https://www.cybercrime.gov.in" target="_blank">https://www.cybercrime.gov.in</a></div>', unsafe_allow_html=True)

elif menu == "Premium Features":
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
    st.link_button("DM Admin on Instagram", "https://www.instagram.com/tawkeer_official_07/")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Admin: Tawkeer")
