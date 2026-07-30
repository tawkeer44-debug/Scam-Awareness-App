import streamlit as st
import time
import random
import re

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind X Pro | PREMIUM", page_icon="💀", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111111; border-right: 2px solid #00FF00; }
    .stTextInput>div>div>input { color: #00FF00; background-color: #000000; }
    .premium-box { border: 2px solid #FFD700; padding: 20px; border-radius: 10px; background-color: #1a1a00; text-align: center; }
    .feature-list { color: #ffffff; text-align: left; }
    h1, h2, h3 { color: #FF0000; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💀 CyberMind Command")
st.sidebar.markdown("---")
menu = st.sidebar.radio("SELECT MODULE", 
    ["Dashboard", "Link Analyzer", "Malware Signature Checker", "IP Locator", "Dark Web Scan", "Premium Plans", "🚨 Emergency"])

# --- Helper Functions ---
def is_url(string):
    regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.match(regex, string) is not None

def simulate_hack(text):
    with st.spinner(f"Initializing {text}..."):
        time.sleep(random.uniform(1.5, 3.0))

# --- Modules ---
if menu == "Dashboard":
    st.title("💻 THREAT INTELLIGENCE CENTER")
    st.info("System Operational. Use modules to scan for threats.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Threats", "3", "+1")
    col2.metric("Nodes Compromised", "1,094", "+56")
    col3.metric("System Integrity", "88%", "-2%")

elif menu == "Link Analyzer":
    st.title("🔍 Phishing URL Analyzer")
    url = st.text_input("Paste URL (e.g., https://example.com):")
    if st.button("SCAN LINK"):
        if is_url(url):
            simulate_hack("Domain Analysis")
            st.error("🔴 HIGH RISK: This URL is flagged as malicious!")
        else:
            st.warning("⚠️ INVALID INPUT: This is not a link. Please enter a valid URL (starting with http:// or https://).")

elif menu == "Malware Signature Checker":
    st.title("🦠 MALWARE SIGNATURE CHECKER")
    file_hash = st.text_input("Enter File Hash (e.g., a1b2c3d4...):")
    if st.button("SCAN FOR MALWARE"):
        if len(file_hash) >= 32:
            simulate_hack("Hash Analysis")
            st.error("🔴 POSITIVE: Signature detected in malware database.")
        else:
            st.warning("⚠️ INVALID INPUT: This is not a hash. Please enter a valid MD5/SHA256 hash (min 32 characters).")

elif menu == "IP Locator":
    st.title("🌐 TARGET IP GEOLOCATION")
    ip = st.text_input("Enter IP (e.g., 192.168.1.1):")
    if st.button("TRACE"):
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            simulate_hack(f"Geo-Locator for {ip}")
            st.success(f"📍 Trace Complete for {ip}. (Simulated Location: US, California)")
        else:
            st.warning("⚠️ INVALID INPUT: This is not an IP. Please enter a correct IP format.")

elif menu == "Dark Web Scan":
    st.title("📡 DARK WEB LEAK MONITOR")
    email = st.text_input("Enter Email:")
    if st.button("SCAN"):
        if "@" in email and "." in email:
            simulate_hack("Deep Web Crawl")
            st.error(f"🚨 BREACH DETECTED for '{email}'.")
        else:
            st.warning("⚠️ INVALID INPUT: This is not an email. Please enter a valid email address.")

elif menu == "Premium Plans":
    st.title("💎 GO PREMIUM")
    
    st.markdown('<div class="feature-list">', unsafe_allow_html=True)
    st.subheader("🚀 Premium Unlocks:")
    features = [
        "✅ Real-time Dark Web Monitoring",
        "✅ Advanced IP Tracking with Map",
        "✅ Priority Malware Database Access",
        "✅ Deep URL Header Analysis",
        "✅ Ad-Free Pro Dashboard",
        "✅ 24/7 Priority Support",
        "✅ Encrypted Data Reports",
        "✅ Bulk Scan Capabilities",
        "✅ Historical Threat Logs",
        "✅ Exclusive Security Guides"
    ]
    for feature in features:
        st.write(feature)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="premium-box">', unsafe_allow_html=True)
    plans = {"7 Days": "₹99", "1 Month": "₹299", "6 Months": "₹1499", "1 Year": "₹2499", "Lifetime": "₹4999"}
    for plan, price in plans.items():
        st.write(f"### {plan}: {price}")
    
    st.markdown("---")
    st.write("### 📩 Want to Upgrade?")
    st.write("DM me on Instagram to unlock Premium:")
    # Yahan apne Instagram ka asli link daal dein
    st.link_button("DM Admin on Instagram", "https://www.instagram.com/your_username_here/") 
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🚨 Emergency":
    st.title("🛡️ IMMEDIATE ACTION PROTOCOL")
    st.error("IF YOU ARE A VICTIM OF FINANCIAL SCAM, DIAL 1930 IMMEDIATELY.")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.caption("CyberMind X Pro")
st.sidebar.info("Admin: Tawkeer")
