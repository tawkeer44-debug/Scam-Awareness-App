import streamlit as st
import random

# --- SETUP ---
st.set_page_config(page_title="CyberMind X", layout="wide")

# --- INITIALIZE STATE ---
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.session_state.is_pro: st.sidebar.success("👑 STATUS: PRO")

# --- FUNCTIONS ---
def add_coins(amount):
    st.session_state.coins += amount

# --- MENU ---
menu = st.sidebar.selectbox("COMMANDS", ["DASHBOARD", "TOOLS", "PRO FEATURES", "REFERRALS"])

# --- DASHBOARD ---
if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    if st.button("🎁 CLAIM DAILY 100"):
        add_coins(100)
        st.rerun()

# --- BASIC TOOLS ---
elif menu == "TOOLS":
    st.header("🛡️ BASIC SECURITY")
    if st.button("Run Scan"):
        add_coins(5)
        st.write("[+] Scan Complete. Safe.")
        st.rerun()

# --- PRO FEATURES ---
elif menu == "PRO FEATURES":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        if st.button("UNLOCK PRO (5000 Coins)"):
            if st.session_state.coins >= 5000:
                st.session_state.coins -= 5000
                st.session_state.is_pro = True
                st.rerun()
            else:
                st.error("Not enough coins!")
    else:
        st.success("✅ PRO FEATURES ACTIVE")
        st.write("1. Kernel Breach")
        st.write("2. WiFi Bypass")
        st.write("3. Database Dump")

# --- REFERRALS ---
elif menu == "REFERRALS":
    st.header("🔗 REFERRAL HUB")
    if st.button("Share with Friend"):
        st.session_state.invite_count += 1
        if st.session_state.invite_count % 15 == 0:
            add_coins(100)
            st.success("Milestone Reached! +100 Coins")
        st.rerun()
