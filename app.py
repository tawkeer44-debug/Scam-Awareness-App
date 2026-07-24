import streamlit as st
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="CyberMind X", layout="wide", page_icon="💀")

# 2. Dark Hacker Terminal Styling
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #000; color: #ff0000; border: 2px solid #ff0000; font-weight: bold; width: 100%; border-radius: 0px; }
    .stButton>button:hover { background-color: #ff0000; color: #fff; }
    h1, h2, h3 { color: #00ff41 !important; text-shadow: 0 0 5px #00ff41; }
    .stCodeBlock { border: 1px solid #00ff41; background-color: #0a0a0a; }
    </style>
""", unsafe_allow_html=True)

# 3. Log Function
def show_hack_log(target, tool_name):
    logs = [
        f"[+] INITIALIZING {tool_name}...",
        f"[+] TARGET IDENTIFIED: {target}",
        "[+] BYPASSING FIREWALL LAYER 1...",
        "[+] PACKET INJECTION SUCCESSFUL...",
        "[+] ANALYZING PROTOCOL HANDSHAKE...",
        "[+] DECRYPTING SECURE HEADERS...",
        "[+] ACCESSING ROOT DIRECTORY...",
        "[+] CONNECTION STABILITY: 98%...",
        "[+] EXTRACTION COMPLETE.",
        "[+] OPERATION FINISHED."
    ]
    st.code("\n".join(logs), language='bash')

# 4. Sidebar - Command Center
st.sidebar.title("💀 COMMAND CENTER")
menu = st.sidebar.selectbox("SELECT OPERATION", [
    "HOME", "THREAT SCANNER", "SYSTEM BREACH", "IP TRACER", "PASSWORD VAULT", 
    "DEEPFAKE SCAN", "PHISHING DETECTOR", "WIFI AUDITOR", "ENCRYPTION TOOL", "PREMIUM HUB"
])

st.title("⚡ CYBERMIND X - DARK OPS")

# 5. Logic for Features
if menu == "HOME":
    st.header("READY FOR ACTION, COMMANDER?")
    st.write("Welcome to the Dark Ops Interface. Choose your weapon from the sidebar.")

elif menu == "THREAT SCANNER":
    st.header("🛡️ THREAT SCANNER")
    target = st.text_input("Enter Link/File:")
    if st.button("RUN SCAN"): show_hack_log(target, "THREAT-SCANNER-V2")

elif menu == "SYSTEM BREACH":
    st.header("💀 SYSTEM BREACH")
    target = st.text_input("Enter Target System ID:")
    if st.button("EXECUTE BREACH"): show_hack_log(target, "KERNEL-BREACH-PROTOCOL")

elif menu == "IP TRACER":
    st.header("📍 IP TRACER")
    target = st.text_input("Enter Target IP:")
    if st.button("TRACE"): show_hack_log(target, "GEO-IP-LOCATOR")

elif menu == "PASSWORD VAULT":
    st.header("🔐 PASSWORD VAULT")
    if st.button("GENERATE SECURE KEY"): st.success(f"KEY: {random.randint(100000, 999999)}-X-CYBER")

elif menu == "DEEPFAKE SCAN":
    st.header("👁️ DEEPFAKE SCANNER")
    st.file_uploader("Upload Image/Video:")
    if st.button("ANALYZE"): st.warning("ANALYSIS: AI Patterns Detected. Caution advised.")

elif menu == "PHISHING DETECTOR":
    st.header("🎣 PHISHING DETECTOR")
    target = st.text_input("Enter suspicious link:")
    if st.button("VERIFY LINK"): show_hack_log(target, "PHISH-SCAN-ALPHA")

elif menu == "WIFI AUDITOR":
    st.header("📶 WIFI SECURITY AUDITOR")
    wifi_name = st.text_input("Enter Wi-Fi Name (SSID):")
    if st.button("RUN SECURITY AUDIT"):
        if wifi_name:
            with st.spinner("Analyzing handshake..."):
                time.sleep(2)
                st.code(f"[+] Target: {wifi_name}\n[+] Encryption: WPA2-AES\n[+] Status: SECURED\n[+] Verdict: Robust Security.", language='bash')
        else: st.warning("Please enter a valid Wi-Fi name.")

elif menu == "ENCRYPTION TOOL":
    st.header("🔒 ENCRYPTION ENGINE")
    text = st.text_input("Message to encrypt:")
    if st.button("ENCRYPT"): st.success("Encoded: QF#23@90-AX-99")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO PRO")
    col1, col2 = st.columns(2)
    with col1: st.markdown("✅ **Unlimited Scans**\n✅ **Root Access**\n✅ **Priority Support**")
    with col2: st.markdown("✅ **Zero Ads**\n✅ **4K Export**\n✅ **Dark Mode Pro**")
    plan = st.radio("SELECT PLAN", ["7 Days - $4.99", "6 Months - $29.99", "1 Year - $49.99", "Lifetime - $99.99"])
    if st.button("ACTIVATE PREMIUM NOW"): 
        st.balloons()
        st.info("Redirecting to secure payment gateway...")
