import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")

if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0
if 'selected_tool' not in st.session_state: st.session_state.selected_tool = None
if 'cmd_input' not in st.session_state: st.session_state.cmd_input = ""

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    input { background-color: #111 !important; color: #00ff41 !important; border: 1px solid #00ff41 !important; }
    </style>
""", unsafe_allow_html=True)

# --- COMMAND CENTER ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.session_state.is_pro: st.sidebar.success("👑 STATUS: PRO")

menu = st.sidebar.selectbox("COMMANDS", [
    "DASHBOARD", "SECURITY LAB", "NETWORK MAPPER", "CRYPTO MINER", 
    "PASSWORD CRACKER", "SYSTEM LOGS", "PRO HACKER SUITE", "REFERRAL HUB"
])

# --- COMMAND EXECUTION ENGINE ---
def run_action(command, cost, reward):
    st.code(f"root@cybermind:~$ {command}")
    with st.spinner("Executing exploit..."):
        time.sleep(1.5)
    st.session_state.coins += reward
    st.success(f"Execution Successful! Balance: +{reward}")
    st.rerun()

# --- INTERFACE ---

if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    if st.button("🎁 CLAIM DAILY 100 COINS"):
        st.session_state.coins += 100
        st.rerun()

elif menu == "SECURITY LAB":
    st.header("🛡️ SECURITY LAB")
    tools = {"Phishing Detector": "scan_phish", "IP Tracker": "trace_ip", "WiFi Audit": "audit_wifi", 
             "Firewall Scan": "check_firewall", "Botnet Check": "scan_botnet", "Deepfake Scan": "scan_ai"}
    
    selected = st.radio("Choose Tool:", list(tools.keys()))
    st.session_state.cmd_input = st.text_input("Enter Command:", value=f"{tools[selected]} --target=target_ip")
    
    if st.button("SUBMIT COMMAND"):
        run_action(st.session_state.cmd_input, 0, 10)

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
        tools = {"Kernel Breach": "exploit_kernel", "WiFi Bypass": "bypass_wpa3", 
                 "Database Dump": "dump_sql", "Firewall Disable": "kill_firewall", 
                 "Root Access": "get_root", "System Override": "override_system"}
        
        selected = st.radio("Choose Pro Tool:", list(tools.keys()))
        st.session_state.cmd_input = st.text_input("Enter Command:", value=f"{tools[selected]} --force")
        
        if st.button("SUBMIT COMMAND"):
            run_action(st.session_state.cmd_input, 0, 50)

elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL HUB")
    st.write(f"Invites: {st.session_state.invite_count}/15")
    st.code("https://cybermind-x.streamlit.app/?ref=tawkeer")
    if st.button("SHARE LINK"):
        st.session_state.invite_count += 1
        st.rerun()

# --- OTHER TOOLS (Same logic as Security Lab) ---
else:
    st.header(f"🔧 {menu.upper()}")
    st.write("Terminal ready for input.")
    st.session_state.cmd_input = st.text_input("Enter Command:", value="help")
    if st.button("RUN"):
        run_action(st.session_state.cmd_input, 0, 20)
