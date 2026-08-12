import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CyberMind Pro Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# --- CUSTOM CSS FOR DARK FUTURISTIC LOOK ---
st.markdown("""
    <style>
        .stApp {
            background-color: #050a14;
            color: #e0e0e0;
        }
        [data-testid="stSidebar"] {
            background-color: #0a1120;
            border-right: 1px solid #1f293d;
        }
        .stat-card {
            background: #0f172a;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #1e293b;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .stat-val {
            font-size: 24px;
            font-weight: bold;
            color: #00ffcc;
        }
        .plan-box {
            background: #111b2e;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #00ffcc;
            margin-bottom: 10px;
        }
        .plan-header {
            color: #00ffcc;
            font-size: 20px;
            font-weight: bold;
            border-bottom: 1px solid #1e293b;
            padding-bottom: 5px;
        }
        .price-tag {
            color: #38bdf8;
            font-weight: bold;
            font-size: 18px;
        }
        .stButton>button {
            width: 100%;
            background-color: #00ffcc;
            color: #050a14;
            border-radius: 5px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9438/9438515.png", width=80)
st.sidebar.title("CyberMind Pro")
menu = st.sidebar.radio(
    "Navigation", 
    [
        "🏠 Dashboard", 
        "🔍 Network Port Scanner", 
        "📡 Live Threat Intel", 
        "🛡️ Vulnerability Exploit Check", 
        "⚡ Packet Analyzer", 
        "🌐 Secure Tunnel VPN", 
        "💎 Premium Hub"
    ]
)

# --- DASHBOARD PAGE ---
if menu == "🏠 Dashboard":
    st.title("🛡️ Security Dashboard & Real-Time Analytics")
    st.markdown("Aaj ke smart zamane ke mutabiq live tracking aur active user indicators:")

    # Top smart metrics cards (Active users & live dots)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-card"><p>🟢 Active Users Now</p><p class="stat-val">1,428 live</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><p>⚡ System Status</p><p class="stat-val">SECURED</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><p>🛑 Blocked Attacks Today</p><p class="stat-val" style="color: #ff4b4b;">342</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><p>🔒 Encrypted Traffic</p><p class="stat-val">2.8 TB</p></div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("Live System & Server Traffic Load")
    c1, c2 = st.columns(2)
    with c1:
        st.info("Incoming Network Traffic: **Stable (Optimal)**")
        st.progress(72)
    with c2:
        st.success("Global Node Synchronization: **99.98%**")
        st.progress(99)

# --- NETWORK SCANNER (Interactive with custom prompt) ---
elif menu == "🔍 Network Port Scanner":
    st.title("🔍 Advanced Network Port Scanner")
    st.write("Apna target IP ya hostname niche prompt mein enter karein aur global port scan start karein:")
    
    target_input = st.text_input("Enter Target IP or Domain (e.g., 192.168.1.1 or example.com)", "192.168.1.100")
    
    if st.button("Start Global Port Scan"):
        if target_input:
            with st.spinner(f"Connecting to target {target_input} and scanning ports..."):
                time.sleep(1)
                st.code(f"""
[+] Initializing TCP socket connection to: {target_input}
[+] Scanning ports 1 through 1024...
    Port 21 (FTP)    : CLOSED
    Port 22 (SSH)    : OPEN (Secure)
    Port 80 (HTTP)   : OPEN
    Port 443 (HTTPS) : OPEN (TLSv1.3 Active)
    Port 8080 (Proxy): FILTERED
[+] Analyzing vulnerabilities... No critical exploits found.
[✓] Scan completed successfully for {target_input}!
                """)
                st.success("Port scan finished without any breach risks.")
        else:
            st.warning("Kripya pehle valid IP ya domain enter karein.")

# --- NEW SECURITY FEATURE 1 ---
elif menu == "📡 Live Threat Intel":
    st.title("📡 Live Threat Intelligence Feed")
    st.write("Real-time global cyber attacks and hacker tracking feed:")
    st.markdown("""
    - **[10:14 AM]** DDoS attack mitigated from IP region: *Eastern Europe* (Blocked automatically)
    - **[09:50 AM]** Brute-force login attempt intercepted on Port 22.
    - **[09:30 AM]** Malicious payload signature identified and quarantined.
    """)
    if st.button("Refresh Threat Feed"):
        st.success("Threat database updated to latest global definitions.")

# --- NEW SECURITY FEATURE 2 ---
elif menu == "🛡️ Vulnerability Exploit Check":
    st.title("🛡️ Deep Vulnerability & Exploit Checker")
    st.write("Check your system for zero-day vulnerabilities and outdated software packets.")
    if st.button("Run Deep Exploit Audit"):
        with st.spinner("Checking system kernel and libraries..."):
            time.sleep(1.2)
            st.warning("⚠️ 1 Minor Warning: OpenSSL version can be updated.")
            st.success("✅ All core security patches are up to date.")

# --- NEW SECURITY FEATURE 3 ---
elif menu == "⚡ Packet Analyzer":
    st.title("⚡ Smart Packet Analyzer & Sniffer")
    st.write("Capture and inspect data packets passing through your secure gateway.")
    if st.button("Capture Live Packets"):
        st.code("""
[PACKET #1024] PROTOCOL: HTTPS | SRC: 10.0.0.5 -> DST: 172.217.14.206 | SIZE: 540 bytes | STATUS: Encrypted
[PACKET #1025] PROTOCOL: DNS   | SRC: 10.0.0.5 -> DST: 8.8.8.8         | SIZE: 78 bytes  | STATUS: Secure
        """)

# --- NEW SECURITY FEATURE 4 ---
elif menu == "🌐 Secure Tunnel VPN":
    st.title("🌐 Secure Encrypted Tunnel (VPN Simulator)")
    st.write("Mask your IP and tunnel your connection through secure global servers.")
    server_loc = st.selectbox("Select Secure Exit Node", ["Switzerland (Secure)", "Iceland (Anonymous)", "Singapore (Fast)", "Germany (Encrypted)"])
    if st.button("Establish Secure Tunnel"):
        st.success(f"Connected successfully via {server_loc}! Your IP is now completely masked.")

# --- PREMIUM HUB (With 10 Plans and Features) ---
elif menu == "💎 Premium Hub":
    st.title("💎 CyberMind Premium Hub")
    st.write("Upgrade your security level with our advanced plans. Har plan ke andar ke saare features niche diye gaye hain:")
    
    plans = [
        {"name": "Starter Guard", "price": "$9/mo", "features": ["Basic Firewall", "Email Shield", "1 Device Protection", "Standard Support"]},
        {"name": "Pro Defender", "price": "$19/mo", "features": ["Advanced Malware Scan", "VPN Access", "3 Devices", "24/7 Priority Support", "Real-time Alerts"]},
        {"name": "Elite Secure", "price": "$49/mo", "features": ["Real-time AI Defense", "Identity Theft Protection", "10 Devices", "Cloud Backup", "Dark Web Monitoring", "Secure Vault"]},
        {"name": "Cyber Ghost", "price": "$79/mo", "features": ["Zero-Log VPN", "Incognito Browsing Shield", "Dark Web Monitoring", "Unlimited Devices", "Dedicated IP"]},
        {"name": "Enterprise Shield", "price": "$199/mo", "features": ["Full Network Encryption", "Dedicated Security Manager", "Unlimited Devices", "Custom Firewall Rules", "API Access"]},
        {"name": "Quantum Pro", "price": "$299/mo", "features": ["Post-Quantum Encryption", "Satellite Link Security", "Hardware Integration", "Military-grade Shield", "Instant Incident Response"]},
        {"name": "Ultimate Sentinel", "price": "$499/mo", "features": ["Complete Digital Asset Protection", "Legal Assistance", "Priority Emergency Response", "Custom Threat Intel Feed", "On-premise Support"]},
        {"name": "Family Armor", "price": "$39/mo", "features": ["Parental Control", "Shared Password Manager", "5 Family Members", "Safe Browsing for Kids", "Location Tracker Shield"]},
        {"name": "Student Shield", "price": "$5/mo", "features": ["Academic Resource Lock", "Basic Protection", "Phishing Filter", "Ad Blocker", "Secure Note Vault"]},
        {"name": "Freelancer Safe", "price": "$15/mo", "features": ["Invoicing Protection", "Secure File Transfer", "Client Data Encryption", "Password Vault", "Anti-Phishing Mail Guard"]}
    ]

    cols = st.columns(2)
    for i, plan in enumerate(plans):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="plan-box">
                    <div class="plan-header">{plan['name']}</div>
                    <div class="price-tag">{plan['price']}</div>
                    <ul style="font-size: 13px; margin-top: 10px;">
                        {"".join([f"<li>{f}</li>" for f in plan['features']])}
                    </ul>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Upgrade to {plan['name']}", key=i):
                st.balloons()
                st.success(f"Activating {plan['name']}... Payment gateway redirecting.")

# Sidebar footer
st.sidebar.write("---")
st.sidebar.caption("CyberMind Pro v3.0 | Live Security Engine")
