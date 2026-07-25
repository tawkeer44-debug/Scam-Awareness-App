import streamlit as st

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

# --- 4. CORE LOGIC ---
def process_invite():
    st.session_state.invite_count += 1
    # Sirf 15 ke set par hi 100 coins
    if st.session_state.invite_count % 15 == 0:
        st.session_state.coins += 100
        st.success(f"🎊 Milestone Hit! 15 friends invited. +100 Coins added!")
    else:
        st.info(f"Progress: {st.session_state.invite_count % 15}/15 friends invited.")

# --- 5. INTERFACE ---
if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    st.write("Welcome to the most dangerous tool on the web.")
    if st.button("🎁 CLAIM DAILY 100 COINS"):
        st.session_state.coins += 100
        st.rerun()

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
        if st.button("UNLOCK PRO (Cost: 5000 Coins)"):
            if st.session_state.coins >= 5000:
                st.session_state.coins -= 5000
                st.session_state.is_pro = True
                st.success("PRO MODE UNLOCKED!")
                st.rerun()
            else:
                st.error("Not enough coins! Need 5000.")
    else:
        # PRO FEATURES
        st.success("✅ PRO FEATURES ACTIVATED!")
        st.button("💀 ROOT KERNEL BREACH")
        st.button("💀 GLOBAL WIFI BYPASS")
        st.button("💀 DATABASE DUMP")
        st.button("💀 FIREWALL DISABLER")
        st.button("💀 SYSTEM OVERRIDE")

elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL SYSTEM")
    st.write("Share with 15 friends to get 100 coins!")
    st.write(f"Your Shares: {st.session_state.invite_count}")
    
    if st.button("📢 Share on WhatsApp"): process_invite()
    if st.button("✈️ Telegram Share"): process_invite()
    if st.button("📸 Instagram Share"): process_invite()
