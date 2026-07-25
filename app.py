import streamlit as st

# --- 1. CONFIG ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")

# --- 2. SESSION STATE (DATABASE) ---
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0
if 'daily_claimed' not in st.session_state: st.session_state.daily_claimed = False

# --- 3. STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.session_state.is_pro: st.sidebar.success("👑 STATUS: PRO ACTIVE")

menu = st.sidebar.selectbox("MODULES", ["DASHBOARD", "SECURITY LAB", "PRO HACKER TOOLS", "REFERRAL HUB"])

# --- 5. LOGIC & FEATURES ---

if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    if not st.session_state.daily_claimed:
        if st.button("🎁 CLAIM DAILY 100 COINS"):
            st.session_state.coins += 100
            st.session_state.daily_claimed = True
            st.rerun()
    else:
        st.write("Daily reward already claimed.")

elif menu == "SECURITY LAB":
    st.header("🛡️ SECURITY LAB")
    tools = ["Phishing Detector", "IP Tracker", "WiFi Security", "System Firewall", "VPN Simulator", "Data Encryptor"]
    for tool in tools:
        if st.button(f"RUN {tool.upper()}"):
            st.session_state.coins += 5
            st.code(f"[+] {tool} EXECUTED SUCCESSFULLY.")
            st.rerun()

elif menu == "PRO HACKER TOOLS":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED. Need 5000 Coins.")
        if st.button("UNLOCK PRO MODE (5000 Coins)"):
            if st.session_state.coins >= 5000:
                st.session_state.coins -= 5000
                st.session_state.is_pro = True
                st.success("UPGRADED!")
                st.rerun()
    else:
        pro_tools = ["Root Access", "Kernel Breach", "WiFi Bypass", "Data Dump", "System Override", "Stealth Mode", "Network Sniffer"]
        for tool in pro_tools:
            st.button(f"💀 EXECUTE {tool.upper()}")

elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL SYSTEM")
    st.write(f"Milestone: Share with 15 friends to get 100 coins. Current Count: {st.session_state.invite_count}")
    
    if st.button("📢 SHARE LINK"):
        st.session_state.invite_count += 1
        if st.session_state.invite_count % 15 == 0:
            st.session_state.coins += 100
            st.success("MILESTONE REACHED! +100 Coins.")
        st.rerun()
