import streamlit as st
import time

# --- 1. CONFIG & SESSION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")

if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0
if 'daily_claimed' not in st.session_state: st.session_state.daily_claimed = False

# --- 2. HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 3. COMMAND CENTER SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.session_state.is_pro: st.sidebar.success("👑 STATUS: PRO")

menu = st.sidebar.selectbox("COMMANDS", ["DASHBOARD", "SECURITY LAB", "PRO HACKER SUITE", "REFERRAL HUB"])

# --- 4. FUNCTIONS ---
def run_command(command_text, reward):
    st.code(f"root@cybermind:~$ {command_text}")
    with st.spinner("Executing..."):
        time.sleep(1.5)
    st.session_state.coins += reward
    st.success(f"Command Executed! Balance Updated: +{reward}")
    st.rerun()

# --- 5. INTERFACE ---

if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    st.write("Welcome back, Commander.")
    
    # Daily Claim Logic Fix
    if not st.session_state.daily_claimed:
        if st.button("🎁 CLAIM DAILY 100 COINS"):
            st.session_state.coins += 100
            st.session_state.daily_claimed = True
            st.rerun()
    else:
        st.warning("✅ Daily Reward already claimed! Come back tomorrow.")

elif menu == "SECURITY LAB":
    st.header("🛡️ SECURITY LAB")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("RUN PHISHING DETECTOR"):
            run_command("scan_phishing --target=url", 10)
    with col2:
        if st.button("RUN IP TRACKER"):
            run_command("trace_ip --ip=192.168.0.1", 10)
    
    with col1:
        if st.button("RUN WIFI SECURITY"):
            run_command("audit_wifi --mode=safe", 10)
    with col2:
        if st.button("RUN FIREWALL SCAN"):
            run_command("check_firewall --status=active", 10)

elif menu == "PRO HACKER SUITE":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED. Need 5000 Coins.")
        if st.button("UNLOCK PRO (5000 Coins)"):
            if st.session_state.coins >= 5000:
                st.session_state.coins -= 5000
                st.session_state.is_pro = True
                st.rerun()
    else:
        st.success("✅ PRO MODE ACTIVATED")
        # Pro Tools with Command Output
        if st.button("💀 KERNEL BREACH"):
            run_command("exploit_kernel --root --force", 50)
        if st.button("💀 WIFI BYPASS"):
            run_command("bypass_wpa3 --auth=null", 50)
        if st.button("💀 DATABASE DUMP"):
            run_command("dump_sql --target=remote_db", 50)

elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL HUB")
    st.write(f"Invite Status: {st.session_state.invite_count}/15")
    st.code("https://cybermind-x.streamlit.app/?ref=tawkeer")
    
    if st.button("📢 SHARE LINK"):
        st.session_state.invite_count += 1
        if st.session_state.invite_count % 15 == 0:
            st.session_state.coins += 100
            st.success("Milestone Reached! +100 Coins.")
        st.rerun()
