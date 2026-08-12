import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CyberMind Pro Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# --- CUSTOM CSS FOR DARK FUTURISTIC LOOK ---
st.markdown("""
    <style>
        /* Main background and text */
        .stApp {
            background-color: #050a14;
            color: #e0e0e0;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0a1120;
            border-right: 1px solid #1f293d;
        }
        
        /* Dashboard Cards */
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
        
        /* Premium Plan Table */
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
        
        /* Buttons */
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
    ["🏠 Dashboard", "🔍 Network Scanner", "🛡️ Firewall Control", "☣️ Malware Vault", "🎙️ Voice AI Control", "💎 Premium Hub", "⚙️ Settings"]
)

# --- DASHBOARD PAGE ---
if menu == "🏠 Dashboard":
    st.title("🛡️ Security Dashboard Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-card"><p>System Status</p><p class="stat-val">SECURED</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><p>Active Threats</p><p class="stat-val" style="color: #ff4b4b;">0</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><p>Data Encrypted</p><p class="stat-val">1.2 TB</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><p>Uptime</p><p class="stat-val">99.9%</p></div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("Live System Diagnostics")
    col_left, col_right = st.columns(2)
    with col_left:
        st.info("Network Traffic Monitoring: **Active**")
        st.progress(85)
        st.info("CPU Usage Monitoring: **Stable**")
        st.progress(24)
    with col_right:
        st.warning("Integrity Check: **Completed**")
        st.success("Firewall Protocol: **AES-256 Active**")

# --- OTHER FEATURES ---
elif menu == "🔍 Network Scanner":
    st.title("🔍 Advanced Network Scanner")
    if st.button("Start Global Port Scan"):
        with st.spinner("Scanning network vulnerability..."):
            st.code("Scanning: 192.168.1.1 ... OK\nScanning: 192.168.1.45 ... SECURE\nThreat detected at: 10.0.0.12 (Blocked)")
            st.success("Scan Completed. System is clean.")

elif menu == "🎙️ Voice AI Control":
    st.title("🎙️ Voice Assistant Control")
    st.write("Control your system with voice commands.")
    st.button("Activate Listening Mode")

# --- PREMIUM HUB (With 10+ Plans and Feature Lists) ---
elif menu == "💎 Premium Hub":
    st.title("💎 CyberMind Premium Hub")
    st.write("Upgrade your security level with our advanced plans.")
    
    plans = [
        {"name": "Starter Guard", "price": "$9/mo", "features": ["Basic Firewall", "Email Shield", "1 Device"]},
        {"name": "Pro Defender", "price": "$19/mo", "features": ["Advanced Malware Scan", "VPN Access", "3 Devices", "24/7 Support"]},
        {"name": "Elite Secure", "price": "$49/mo", "features": ["Real-time AI Defense", "Identity Theft Protection", "10 Devices", "Cloud Backup"]},
        {"name": "Cyber Ghost", "price": "$79/mo", "features": ["Zero-Log VPN", "Incognito Browsing Shield", "Dark Web Monitoring"]},
        {"name": "Enterprise Shield", "price": "$199/mo", "features": ["Full Network Encryption", "Dedicated Security Manager", "Unlimited Devices"]},
        {"name": "Quantum Pro", "price": "$299/mo", "features": ["Post-Quantum Encryption", "Satellite Link Security", "Hardware Integration"]},
        {"name": "Ultimate Sentinel", "price": "$499/mo", "features": ["Complete Digital Asset Protection", "Legal Assistance", "Priority Emergency Response"]},
        {"name": "Family Armor", "price": "$39/mo", "features": ["Parental Control", "Shared Password Manager", "5 Family Members"]},
        {"name": "Student Shield", "price": "$5/mo", "features": ["Academic Resource Lock", "Basic Protection", "Phishing Filter"]},
        {"name": "Freelancer Safe", "price": "$15/mo", "features": ["Invoicing Protection", "Secure File Transfer", "Client Data Encryption"]}
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
                st.success(f"Activating {plan['name']}... Please complete payment.")

elif menu == "⚙️ Settings":
    st.title("⚙️ System Settings")
    st.toggle("Auto-Update Security Protocols")
    st.toggle("Dark Web Alerts")
    st.selectbox("Data Backup Frequency", ["Every 1 hour", "Daily", "Weekly"])

# Footer
st.sidebar.write("---")
st.sidebar.caption("CyberMind Pro v2.0.4")
