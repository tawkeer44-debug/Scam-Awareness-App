import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="CyberMind X", layout="wide")

# --- INITIALIZING ECONOMY ---
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'reward_claimed' not in st.session_state: st.session_state.reward_claimed = False

# --- UI STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: ECONOMY DASHBOARD ---
st.sidebar.title("💰 CYBER-WALLET")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.sidebar.button("🎁 Daily 50 Coins"):
    if not st.session_state.reward_claimed:
        st.session_state.coins += 50
        st.session_state.reward_claimed = True
        st.sidebar.success("Reward Claimed!")
    else: st.sidebar.warning("Already claimed!")

# --- MAIN MENU ---
menu = st.sidebar.selectbox("COMMAND CENTER", [
    "HOME", "THREAT SCANNER", "SYSTEM BREACH", "WIFI PASSWORD SIMULATOR", "REFERRAL HUB"
])

st.title("⚡ CYBERMIND X - DARK OPS")

# --- LOGIC FOR ALL FEATURES ---
if menu == "HOME":
    st.write("Welcome to the most advanced security tool. Scan, Breach, and Earn!")

elif menu == "THREAT SCANNER":
    st.header("🛡️ THREAT SCANNER")
    target = st.text_input("Enter Link:")
    if st.button("RUN SCAN"):
        st.session_state.coins += 5 # User ko scan karne ke coins milenge
        st.code("[+] SCANNING: " + target + "\n[+] RESULT: SAFE")

elif menu == "SYSTEM BREACH":
    st.header("💀 SYSTEM BREACH")
    target = st.text_input("Target ID:")
    if st.button("EXECUTE"):
        st.session_state.coins += 10
        st.code("[+] BREACH SUCCESSFUL\n[+] COINS EARNED: 10")

elif menu == "WIFI PASSWORD SIMULATOR":
    st.header("💀 WIFI SIMULATOR")
    wifi = st.text_input("Enter SSID:")
    if st.button("EXTRACT"):
        st.session_state.coins += 20
        password = f"X-{random.randint(1000,9999)}-{wifi[:3].upper()}"
        st.code(f"[+] PASSWORD: {password}\n[+] COINS EARNED: 20")

elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL SYSTEM")
    ref = st.text_input("Enter Referral Code:")
    if st.button("REDEEM"):
        if ref == "PRO2026":
            st.session_state.coins += 100
            st.success("Referral Applied! +100 Coins")
        else: st.error("Invalid Code")

st.sidebar.info("Tip: Use tools to earn more coins!")
