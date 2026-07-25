import streamlit as st
import random
import time

# --- CONFIG & ECONOMY ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'last_reward' not in st.session_state: st.session_state.last_reward = None

# --- UI STYLING (HACKER THEME) ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; }
    .stButton>button:hover { background: #00ff41; color: #000; }
    </style>
""", unsafe_allow_html=True)

# --- DAILY REWARD LOGIC ---
st.sidebar.title("💎 CYBER-WALLET")
st.sidebar.metric("Coins", f"{st.session_state.coins} 🪙")
if st.sidebar.button("🎁 CLAIM DAILY 100 COINS"):
    st.session_state.coins += 100
    st.sidebar.success("100 Coins Added!")

# --- MASTER MENU ---
menu = st.sidebar.selectbox("COMMAND CENTER", [
    "SECURITY SUITE", "HACKER TOOLS", "SOCIAL SHARING", "PREMIUM UPGRADE"
])

# --- SECURITY SUITE ---
if menu == "SECURITY SUITE":
    st.header("🛡️ SECURITY SUITE")
    tools = ["Phishing Detector", "System Scanner", "IP Tracker", "Deepfake Scanner"]
    choice = st.selectbox("Select Tool:", tools)
    if st.button("RUN ANALYSIS"):
        st.session_state.coins += 5
        st.code(f"[+] ANALYZING {choice.upper()}...\n[+] STATUS: SECURE (Coins +5)")

# --- HACKER TOOLS ---
elif menu == "HACKER TOOLS":
    st.header("💀 HACKER TOOLS")
    target = st.text_input("Enter Target Name/IP:")
    if st.button("WIFI SIMULATOR"):
        st.session_state.coins += 20
        password = f"X-{random.randint(1000,9999)}"
        st.code(f"[+] TARGET: {target}\n[+] PASS: {password}\n[+] COINS EARNED: 20")

# --- SOCIAL SHARING (REFERRAL HUB) ---
elif menu == "SOCIAL SHARING":
    st.header("🔗 INVITE & EARN")
    st.write("Share CyberMind X with friends to earn 500 coins!")
    
    # Sharing URLs
    share_text = "Check out this insane CyberMind X Security App! Download here: https://your-app-link.com"
    wa_url = f"https://wa.me/?text={share_text}"
    tg_url = f"https://t.me/share/url?url=https://your-app-link.com&text={share_text}"
    ig_url = "https://www.instagram.com/" # Instagram requires direct app interaction
    
    col1, col2, col3 = st.columns(3)
    with col1: st.link_button("WhatsApp", wa_url)
    with col2: st.link_button("Telegram", tg_url)
    with col3: st.link_button("Instagram", ig_url)

# --- PREMIUM UPGRADE ---
elif menu == "PREMIUM UPGRADE":
    st.header("👑 UPGRADE TO PRO")
    st.write("Unlock secret hacker modes and unlimited scans.")
    if st.button("BUY PRO (5000 COINS)"):
        if st.session_state.coins >= 5000:
            st.session_state.coins -= 5000
            st.balloons()
            st.success("Welcome to Pro Mode!")
        else:
            st.error("Not enough coins!")
