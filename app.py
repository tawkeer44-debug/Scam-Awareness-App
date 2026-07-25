import streamlit as st
import random

# --- 1. CONFIG & SESSION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0

# --- 2. HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stButton>button:hover { background: #00ff41; color: #000; }
    </style>
""", unsafe_allow_html=True)

# --- 3. COMMAND CENTER ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.session_state.is_pro: st.sidebar.success("👑 STATUS: PRO MEMBER")

menu = st.sidebar.selectbox("SELECT OPERATION", [
    "DASHBOARD", "BASIC TOOLS", "PRO HACKER TOOLS", "REFERRAL HUB"
])

# --- 4. LOGIC ---
def process_invite():
    st.session_state.invite_count += 1
    if st.session_state.invite_count % 15 == 0:
        st.session_state.coins += 100
        st.success("Milestone Hit! +100 Coins.")

# --- 5. INTERFACE ---
if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    st.write("Welcome to the most dangerous tool on the web.")
    if st.button("🎁 CLAIM DAILY 100 COINS"):
        st.session_state.coins += 100
        st.experimental_rerun()

elif menu == "BASIC TOOLS":
    st.header("🛡️ BASIC SECURITY")
    if st.button("Phishing Scanner"):
        st.code("[+] SCANNING... SAFE.")
        st.session_state.coins += 5
    if st.button("IP Trace"):
        st.code("[+] TRACING IP... 192.168.1.1")
        st.session_state.coins += 5

elif menu == "PRO HACKER TOOLS":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED! Upgrade to access.")
        if st.button("UNLOCK PRO (Cost: 500 Coins)"):
            if st.session_state.coins >= 500:
                st.session_state.coins -= 500
                st.session_state.is_pro = True
                st.success("PRO MODE UNLOCKED!")
                st.experimental_rerun()
    else:
        # YEH FEATURES SIRF PRO KO DIKHENGE
        st.success("PRO FEATURES ACTIVATED!")
        if st.button("💀 ROOT KERNEL BREACH"):
            st.code("[+] BREAKING ENCRYPTION...\n[+] ROOT ACCESS GRANTED!")
        if st.button("💀 GLOBAL WIFI BYPASS"):
            st.code("[+] BYPASSING WPA3...\n[+] GATEWAY ACCESSED!")
        if st.button("💀 DATABASE DUMP"):
            st.code("[+] DUMPING DATA...\n[+] 500MB EXTRACTED!")

elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL SYSTEM")
    st.write(f"Total Invites: {st.session_state.invite_count}")
    if st.button("📢 Share on WhatsApp"): process_invite()
    if st.button("✈️ Share on Telegram"): process_invite()
