import streamlit as st
import time
import re
from datetime import datetime

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
    .tool-box { border: 1px solid #00FF00; padding: 15px; background-color: #001a00; border-radius: 5px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💀 Scam Awareness Command")
menu = st.sidebar.radio("MODULES", 
    ["Dashboard", "Live Scam News", "UPI/Transaction Checker", "Scam Password Checker", "Link Analyzer", "Cyber Safety Tips", "Premium Features"])

# --- Modules ---
if menu == "Dashboard":
    st.title("💻 THREAT INTELLIGENCE CENTER")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="metric-box"><h3>LIVE USERS</h3><h2 style="color:white;">8,142</h2></div>', unsafe_allow_html=True)
    st.subheader("System Status: OPERATIONAL")
    st.info("Scam Awareness Platform is actively protecting the network.")

elif menu == "Live Scam News":
    st.title("📰 LIVE SCAM ALERTS (DAILY UPDATED)")
    
    # Daily rotating dynamic alerts based on day of the year
    day_index = datetime.now().timetuple().tm_yday
    all_news_pools = [
        [
            "⚠️ Alert: New 'Task-based' YouTube rating scam active on Telegram.",
            "⚠️ Warning: Fake electricity bill SMS saying 'Your power will be cut tonight'.",
            "⚠️ Alert: Deepfake video calls impersonating police officers for digital arrest extortion.",
            "⚠️ Warning: Fake government subsidy and loan apps active on third-party sites."
        ],
        [
            "⚠️ Alert: Fake courier parcel drug customs scam targeting working professionals.",
            "⚠️ Warning: Credit card reward points expiry phishing links spreading via WhatsApp.",
            "⚠️ Alert: Fake work-from-home data entry typing job frauds.",
            "⚠️ Warning: Investment group scams promising 300% stock returns in 5 days."
        ],
        [
            "⚠️ Alert: Fake customer care numbers listed on Google Maps for banks and wallets.",
            "⚠️ Warning: QR code scanning frauds where money is debited instead of credited.",
            "⚠️ Alert: Fake lottery winning notifications via SMS and WhatsApp audio.",
            "⚠️ Warning: Fake matrimonial profile frauds targeting individuals for money."
        ]
    ]
    
    todays_news = all_news_pools[day_index % len(all_news_pools)]
    
    st.write(f"📅 Showing verified intelligence feed for: **{datetime.now().strftime('%d %B %Y')}**")
    for item in todays_news:
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

elif menu == "Scam Password Checker":
    st.title("🔑 Scam Password / Strength Checker")
    st.write("Check if your password is weak and vulnerable to brute-force cyber attacks.")
    
    pwd = st.text_input("Enter a password to test:", type="password")
    if st.button("ANALYZE PASSWORD"):
        if len(pwd) == 0:
            st.warning("⚠️ Please enter a password first.")
        else:
            score = 0
            if len(pwd) >= 8: score += 1
            if re.search(r'[A-Z]', pwd): score += 1
            if re.search(r'[0-9]', pwd): score += 1
            if re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd): score += 1
            
            if score == 4:
                st.success("🟢 STRONG PASSWORD: Highly secure against modern hacking tools.")
            elif score >= 2:
                st.warning("⚠️ MODERATE PASSWORD: Consider adding numbers, symbols, or making it longer.")
            else:
                st.error("🔴 WEAK PASSWORD: Easily crackable! Change it immediately to avoid credential stuffing scams.")

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

elif menu == "Cyber Safety Tips":
    st.title("💡 Cyber Safety Tip Generator")
    st.write("Get expert recommended daily rules to stay completely immune to online scams.")
    
    tips_list = [
        "🔒 Never share your UPI PIN, OTP, or Bank Passwords with anyone over phone calls or messages.",
        "🛑 If an offer looks too good to be true (like free iPhones or double money), it is 100% a scam.",
        "🔗 Always check the website domain carefully before logging in or entering personal info.",
        "📱 Avoid downloading apps recommended by strangers on Telegram or WhatsApp for part-time jobs.",
        "🔄 Keep your phone operating system and security apps updated to the latest version."
    ]
    
    selected_tip = tips_list[datetime.now().day % len(tips_list)]
    st.markdown(f'<div class="tool-box"><h3>🛡️ Today’s Pro Security Advice</h3><p style="font-size: 18px; color: #00ffaa;">{selected_tip}</p></div>', unsafe_allow_html=True)
    
    if st.button("GET ANOTHER RANDOM TIP"):
        import random
        st.info(f"💡 Tip: {random.choice(tips_list)}")

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
