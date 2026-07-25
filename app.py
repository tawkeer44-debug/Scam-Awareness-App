import streamlit as st
import time
import random

# --- CONFIG ---
st.set_page_config(page_title="CyberMind X", layout="wide")

# --- INITIALIZE SESSION ---
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0

# --- REFERRAL RECOGNITION ---
# Yeh code link ke parameter (?ref=...) ko padhta hai
query_params = st.query_params
if "ref" in query_params:
    st.session_state.invite_count += 1
    st.success("Referral link recognized! Count updated.")
    st.query_params.clear() # Link saaf kar do taaki baar baar add na ho

# --- CORE FUNCTION: COMMAND EXECUTION ---
def execute_hack(tool_name):
    st.write(f"--- INITIALIZING {tool_name} ---")
    with st.spinner(f"Running {tool_name}..."):
        time.sleep(2) # Fake loading time
        st.code(f"[+] SUCCESS: {tool_name} executed.\n[+] Access granted to target node.\n[+] Coins added: +50")
    st.session_state.coins += 50
    st.rerun()

# --- STYLING ---
st.markdown("<style>.stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")

menu = st.sidebar.selectbox("COMMANDS", ["DASHBOARD", "SECURITY LAB", "PRO HACKER SUITE", "REFERRAL HUB"])

# --- DASHBOARD ---
if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    if st.button("🎁 CLAIM DAILY 100"):
        st.session_state.coins += 100
        st.success("Daily Reward Added!")
        st.rerun()

# --- SECURITY LAB ---
elif menu == "SECURITY LAB":
    st.header("🛡️ SECURITY LAB")
    tools = ["Phishing Detector", "IP Tracker", "WiFi Security", "Botnet Scanner"]
    for tool in tools:
        if st.button(f"RUN {tool}"):
            st.session_state.coins += 10
            st.code(f"[+] {tool} finished. System clean.")
            st.rerun()

# --- PRO HACKER SUITE ---
elif menu == "PRO HACKER SUITE":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED! Need 5000 Coins.")
        if st.button("UNLOCK PRO MODE"):
            if st.session_state.coins >= 5000:
                st.session_state.coins -= 5000
                st.session_state.is_pro = True
                st.rerun()
    else:
        pro_tools = ["Kernel Breach", "WiFi Bypass", "Database Dump", "Firewall Disable"]
        for tool in pro_tools:
            if st.button(f"EXECUTE {tool}"):
                execute_hack(tool)

# --- REFERRAL HUB ---
elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL HUB")
    st.write(f"Current Invites: {st.session_state.invite_count}/15")
    st.write("Share this link with friends:")
    st.code("https://cybermind-x.streamlit.app/?ref=tawkeer")
    
    if st.session_state.invite_count >= 15:
        st.session_state.coins += 100
        st.session_state.invite_count = 0 # Reset for next 100 coins
        st.success("15 friends reached! +100 Coins added.")
        st.rerun()
