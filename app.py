import streamlit as st
import time
import random

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind X Pro | ULTIMATE", page_icon="💀", layout="wide")

# --- Custom CSS (Hacker Style) ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111111; border-right: 2px solid #00FF00; }
    .stTextInput>div>div>input { color: #00FF00; background-color: #000000; }
    .stSelectbox>div>div>select { color: #00FF00; background-color: #000000; }
    .stTextArea>div>div>textarea { color: #00FF00; background-color: #000000; }
    h1, h2, h3 { color: #FF0000; } 
    .metric-card { background-color: #1c1c1c; border: 1px solid #333; padding: 15px; border-radius: 5px; }
    .khatarnak-box { border: 2px solid #FF0000; padding: 10px; border-radius: 5px; background-color: #2a0000; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💀 CyberMind Command")
st.sidebar.markdown("---")
menu = st.sidebar.radio("SELECT MODULE", 
    ["Dashboard", "IP Locator", "Malware Signature Checker", "Dark Web Scan", "Header Check", "Link Analyzer", "Report a Scam", "🚨 Emergency"])

# --- Helper Functions ---
def simulate_hack(text):
    with st.spinner(f"Initializing {text}..."):
        time.sleep(random.uniform(1.5, 3.0))

# --- Modules ---
if menu == "Dashboard":
    st.title("💻 THREAT INTELLIGENCE CENTER")
    with st.expander("🚨 CRITICAL VULNERABILITIES (LIVE)", expanded=True):
        st.error("ZERO-DAY EXPLOIT DETECTED in OpenSSL [CVE-2023-XXXX]")
        st.warning("Ransomware Node 'BlackMatter' Active in Geo-Zone: Asia")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Threats", "3", "+1")
    col2.metric("Nodes Compromised", "1,094", "+56")
    col3.metric("System Integrity", "88%", "-2%")

elif menu == "IP Locator":
    st.title("🌐 TARGET IP GEOLOCATION")
    ip_input = st.text_input("Enter IP Address:", placeholder="8.8.8.8")
    if st.button("TRACE IP"):
        if ip_input:
            simulate_hack(f"Geo-Locator for {ip_input}")
            st.success("Trace Complete.")
            st.markdown(f'<div class="metric-card"><h3>📍 IP Details: {ip_input}</h3><p>ISP: Global ISP</p><p>Country: US</p></div>', unsafe_allow_html=True)

# NEW FEATURE: Malware Signature Checker
elif menu == "Malware Signature Checker":
    st.title("🦠 MALWARE SIGNATURE CHECKER")
    file_input = st.text_input("Upload/Enter File Hash (MD5/SHA256):")
    if st.button("SCAN FOR MALWARE"):
        if file_input:
            simulate_hack("Hash Analysis against VirusTotal Database")
            st.warning("Scanning...")
            time.sleep(1)
            st.error("🔴 POSITIVE: This signature matches known Trojan/Ransomware variants.")
            st.write("Description: Trojan.Generic.30219")
        else:
            st.error("Please enter a file hash to scan.")

elif menu == "Dark Web Scan":
    st.title("📡 DARK WEB LEAK MONITOR")
    target = st.text_input("Enter Email to Scan:")
    if st.button("SCAN DEEP WEB"):
        simulate_hack("Deep Web Crawl")
        st.error(f"🚨 BREACH DETECTED for '{target}' in 3 databases.")

elif menu == "Header Check":
    st.title("🕵️‍♂️ HTTP SECURITY HEADER INVESTIGATOR")
    url = st.text_input("Enter URL:", placeholder="https://google.com")
    if st.button("INSPECT HEADERS"):
        simulate_hack("Header Analysis")
        st.success("Analysis Complete: Secure Headers Detected.")

elif menu == "Link Analyzer":
    st.title("🔍 Phishing URL Analyzer")
    url = st.text_input("Paste suspect URL:")
    if st.button("Scan Link"):
        simulate_hack("Blacklist Check")
        st.error("🔴 HIGH RISK: Domain flagged.")

elif menu == "Report a Scam":
    st.title("🚨 Submit Intelligence Report")
    details = st.text_area("Scam Details:")
    if st.button("Transmit Report"):
        st.success("Report transmitted to central node.")

elif menu == "🚨 Emergency":
    st.title("🛡️ IMMEDIATE ACTION PROTOCOL")
    st.error("IF YOU ARE A VICTIM OF FINANCIAL SCAM, DIAL 1930 IMMEDIATELY.")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.caption("CyberMind X Pro | For Educational Use Only")
st.sidebar.info("Admin: Tawkeer")
