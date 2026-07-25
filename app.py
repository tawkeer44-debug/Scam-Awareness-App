import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- SESSION STATE ---
if 'is_pro' not in st.session_state: st.session_state.is_pro = False

# --- HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- DETAILED ENGINE (NO DELAY) ---
def get_hacker_response(tool, cmd):
    return f"""
    [SYSTEM]: Protocol Initiated for {tool}
    [COMMAND]: {cmd}
    --------------------------------------------------------
    [1] Establishing encrypted socket connection...
    [2] Bypassing target perimeter defenses (v9.4)...
    [3] Scanning memory registers for overflow vulnerabilities...
    [4] Detected active firewall; deploying stealth evasion patch...
    [5] Hash identification successful: SHA-256 (SALTED)...
    [6] Root privilege elevation complete (UID: 0)...
    [7] Injecting diagnostic payload for deep system analysis...
    [8] Data extraction stream stabilized at 1.2 GB/s...
    [9] Tokenized session capture successfully retrieved...
    [10] FINAL STATUS: Target Compromised & Data Downloaded.
    """

# --- SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "FORENSICS", "CRYPTO MINER", "TRAFFIC MONITOR", 
    "PRO HACKER SUITE", "PREMIUM HUB"
])

# --- GENERIC TOOL FUNCTION ---
def run_tool_section(title, options, default_cmd_suffix="--exec"):
    st.header(f"🛡️ {title}")
    choice = st.selectbox("Select Tool:", options)
    cmd = st.text_input("Enter Command:", value=f"{choice.lower().replace(' ', '_')} {default_cmd_suffix}")
    
    if st.button("SUBMIT COMMAND"):
        st.code(get_hacker_response(choice, cmd))

# --- APP LOGIC ---

if menu == "SECURITY LAB":
    run_tool_section("SECURITY LAB", ["Phishing Detector", "IP Trace", "WiFi Audit", "Firewall Check"])

elif menu == "NETWORK MAPPER":
    run_tool_section("NETWORK MAPPER", ["Port Scan", "Subnet Discovery", "DNS Enumeration", "Host Sweep"])

elif menu == "PASSWORD CRACKER":
    run_tool_section("PASSWORD CRACKER", ["Brute Force", "Dictionary Attack", "Hash Decryption", "Rainbow Table"])

elif menu == "FORENSICS":
    run_tool_section("FORENSICS", ["Kernel Dump", "Log Analysis", "Memory Dump", "Disk Imaging"])

elif menu == "CRYPTO MINER":
    run_tool_section("CRYPTO MINER", ["Hashrate Test", "Wallet Audit", "Node Sync", "Block Verify"])

elif menu == "TRAFFIC MONITOR":
    run_tool_section("TRAFFIC MONITOR", ["Packet Sniffer", "Bandwidth Log", "Connection Trace", "Protocol Analyzer"])

# --- PRO HACKER SUITE ---
elif menu == "PRO HACKER SUITE":
    st.header("💀 PRO HACKER SUITE")
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED.")
        if st.button("UNLOCK PRO ACCESS"):
            st.session_state.is_pro = True
            st.rerun()
    else:
        st.success("✅ PRO ACCESS GRANTED")
        pro_tools = ["Kernel Breach", "WiFi Bypass", "DB Dump", "Brute Force", "Traffic Spoof", "System Override"]
        choice = st.selectbox("Select Pro Tool:", pro_tools)
        cmd = st.text_input("Enter Command:", value=f"{choice.lower().replace(' ', '_')} --root --force")
        if st.button("SUBMIT COMMAND"):
            st.code(get_hacker_response(choice, cmd))

# --- PREMIUM HUB ---
elif menu == "PREMIUM HUB":
    st.header("💎 PREMIUM HUB")
    st.write("Select your plan to unlock full potential:")
    
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    
    st.write(f"--- You selected: **{plan}** ---")
    st.write("To proceed with payment and activation, please contact me directly on Instagram.")
    
    # DM Link configured for your Instagram
    st.link_button(f"Message me for {plan} Plan", f"https://ig.me/m/th3_tawkeer")
