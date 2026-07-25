import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")

# --- INITIALIZE STATE ---
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'daily_claimed' not in st.session_state: st.session_state.daily_claimed = False
if 'invite_count' not in st.session_state: st.session_state.invite_count = 0

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- DETAILED RESPONSE GENERATOR ---
def generate_hacker_output(tool_name, command):
    output = f"""
    [SYSTEM] Executing: {tool_name}
    [COMMAND] {command}
    --------------------------------------------------
    [INFO] Initializing secure handshake...
    [SECURE] Encrypted tunnel established at 256-bit AES.
    [PACKET] Analyzing headers from target node...
    [STATUS] Bypassing primary firewall barriers.
    [LOG] Access granted to restricted system directory.
    [WARNING] Root privileges confirmed.
    [DATA] Extracting encrypted configuration keys...
    [RESULT] Operation complete. Target compromised.
    --------------------------------------------------
    [SUCCESS] 50 Coins credited to your wallet.
    """
    return output

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("💀 COMMAND CENTER")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")
if st.session_state.is_pro: st.sidebar.success("👑 STATUS: PRO ACTIVE")

menu = st.sidebar.selectbox("COMMANDS", [
    "DASHBOARD", "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "CRYPTO MINER", "SYSTEM LOGS", "PRO HACKER SUITE", "REFERRAL HUB"
])

# --- DASHBOARD LOGIC ---
if menu == "DASHBOARD":
    st.title("⚡ CYBERMIND X")
    st.write("Welcome back, Commander. Status: ACTIVE.")
    if not st.session_state.daily_claimed:
        if st.button("🎁 CLAIM DAILY 100 COINS"):
            st.session_state.coins += 100
            st.session_state.daily_claimed = True
            st.rerun()
    else:
        st.warning("✅ Reward Already Claimed for today. Return tomorrow!")

# --- SECURITY LAB & OTHERS (Generic Executor) ---
elif menu in ["SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", "CRYPTO MINER", "SYSTEM LOGS"]:
    st.header(f"🛡️ {menu}")
    tool_options = {
        "SECURITY LAB": ["Phishing Scan", "IP Trace", "Firewall Check", "Botnet Scan"],
        "NETWORK MAPPER": ["Port Scan", "Subnet Discovery", "Traffic Analysis", "DNS Enumeration"],
        "PASSWORD CRACKER": ["Brute Force", "Dictionary Attack", "Hash Decryption", "Rainbow Table"],
        "CRYPTO MINER": ["Hashrate Test", "Wallet Audit", "Block Verify", "Node Sync"],
        "SYSTEM LOGS": ["Kernel Dump", "Error Report", "Auth Logs", "Root Events"]
    }
    
    choice = st.selectbox("Select Tool:", tool_options[menu])
    cmd = st.text_input("Enter Command:", value=f"{choice.lower().replace(' ', '_')} --run")
    
    if st.button("SUBMIT COMMAND"):
        with st.spinner("Processing..."):
            time.sleep(1.5)
            st.code(generate_hacker_output(choice, cmd))
            st.session_state.coins += 50
            st.rerun()

# --- PRO HACKER SUITE ---
elif menu == "PRO HACKER SUITE":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED. Need 5000 Coins.")
        if st.button("UNLOCK PRO MODE (5000 Coins)"):
            if st.session_state.coins >= 5000:
                st.session_state.coins -= 5000
                st.session_state.is_pro = True
                st.rerun()
            else:
                st.error("Not enough coins!")
    else:
        pro_tools = ["Kernel Breach", "WiFi Bypass", "Database Dump", "Firewall Disable", "System Override", "Stealth Mode"]
        choice = st.selectbox("Select Pro Tool:", pro_tools)
        cmd = st.text_input("Enter Command:", value=f"{choice.lower().replace(' ', '_')} --force --root")
        
        if st.button("SUBMIT COMMAND"):
            with st.spinner("Executing exploit..."):
                time.sleep(1.5)
                st.code(generate_hacker_output(choice, cmd))
                st.session_state.coins += 100
                st.rerun()

# --- REFERRAL HUB ---
elif menu == "REFERRAL HUB":
    st.header("🔗 REFERRAL HUB")
    st.write(f"Invites: {st.session_state.invite_count}/15")
    st.code("https://cybermind-x.streamlit.app/?ref=tawkeer")
    if st.button("SHARE LINK"):
        st.session_state.invite_count += 1
        if st.session_state.invite_count % 15 == 0:
            st.session_state.coins += 100
            st.success("Milestone Hit! +100 Coins.")
        st.rerun()
