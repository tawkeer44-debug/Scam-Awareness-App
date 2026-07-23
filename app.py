import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="CyberMind X", layout="wide", page_icon="💀")

# 2. Dark Hacker Styling
st.markdown("""
    <style>
    .stApp { background: #000000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { background: #000; color: #ff0000; border: 2px solid #ff0000; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background: #111; color: #00ff41; border: 1px solid #00ff41; }
    code { color: #ff0000 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Helper Function for 5-10 line output
def show_hack_log(target, tool_name):
    logs = [
        f"[+] Initializing {tool_name}...",
        f"[+] Target Identified: {target}",
        "[+] Bypassing Firewall Layer 1...",
        "[+] Packet Injection Successful...",
        "[+] Analyzing Protocol Handshake...",
        "[+] Decrypting Secure Headers...",
        "[+] Accessing Root Directory...",
        "[+] Connection Stability: 98%...",
        "[+] Extraction Complete.",
        "[+] Operation Finished."
    ]
    st.code("\n".join(logs), language='bash')

# 4. Sidebar Modules
st.sidebar.title("💀 COMMAND CENTER")
menu = st.sidebar.selectbox("SELECT MODULE", [
    "THREAT SCANNER", "SYSTEM BREACH", "IP TRACER", "PASSWORD CRACKER", 
    "PHISHING DETECTOR", "WIFI SNIFFER", "ENCRYPTION ENGINE", "DEEPFAKE ANALYZER",
    "NETWORK SNIFFER", "PREMIUM HUB"
])

st.title(f"⚡ CYBERMIND X: {menu}")

# 5. Logic
if menu == "THREAT SCANNER":
    target = st.text_input("Enter File Path/Link:")
    if st.button("RUN SCAN"):
        with st.spinner("Processing..."):
            time.sleep(2)
            show_hack_log(target, "Threat-Scanner-v2")

elif menu == "SYSTEM BREACH":
    target = st.text_input("Enter Target System ID:")
    if st.button("EXECUTE BREACH"):
        show_hack_log(target, "Kernel-Breach-Protocol")

elif menu == "IP TRACER":
    target = st.text_input("Enter Target IP Address:")
    if st.button("TRACE IP"):
        show_hack_log(target, "Geo-IP-Locator")

elif menu == "PASSWORD CRACKER":
    target = st.text_input("Enter Encrypted Hash:")
    if st.button("CRACK PASSWORD"):
        show_hack_log(target, "Hash-Brute-Force")

elif menu == "PHISHING DETECTOR":
    target = st.text_input("Enter Suspicious URL:")
    if st.button("DETECT"):
        show_hack_log(target, "Phish-Scan-Alpha")

elif menu == "WIFI SNIFFER":
    target = st.text_input("Enter WiFi SSID:")
    if st.button("SNIFF"):
        show_hack_log(target, "WPA2-Sniffer")

elif menu == "ENCRYPTION ENGINE":
    target = st.text_input("Enter Message:")
    if st.button("ENCRYPT"):
        show_hack_log(target, "AES-256-Encryptor")

elif menu == "DEEPFAKE ANALYZER":
    target = st.text_input("Enter Media Link:")
    if st.button("ANALYZE"):
        show_hack_log(target, "AI-Pattern-Analyzer")

elif menu == "NETWORK SNIFFER":
    target = st.text_input("Enter Server IP:")
    if st.button("SNIFF PACKETS"):
        show_hack_log(target, "Packet-Interceptor")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO PRO")
    st.write("Unlock 10+ Advanced Modules & 8K Exports.")
    plan = st.radio("CHOOSE PLAN", ["7 Days ($4.99)", "6 Months ($29.99)", "1 Year ($49.99)", "Lifetime ($99.99)"])
    if st.button("ACTIVATE PREMIUM"):
        st.balloons()
        st.success("Redirecting to secure gateway...")
