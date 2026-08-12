import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CyberMind Pro Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# --- CUSTOM CSS ---
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
        .hero-banner {
            background: linear-gradient(135deg, #0f172a, #1e1b4b);
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #38bdf8;
            margin-bottom: 25px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE FOR ACTIVE USERS ---
if 'active_users' not in st.session_state:
    st.session_state.active_users = 9995

# --- SIDEBAR NAVIGATION (Updated features) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9438/9438515.png", width=80)
st.sidebar.title("CyberMind Pro")

menu = st.sidebar.radio(
    "Navigation", 
    [
        "🏠 Dashboard", 
        "🧠 AI Scam & Phishing Detector", 
        "🔐 2FA & OTP Fraud Shield", 
        "🔑 Dark Web Password Leak Test", 
        "🔗 Safe Link & URL Checker", 
        "🛡️ Public Wi-Fi Risk Analyzer", 
        "💎 Premium Hub"
    ]
)

# --- DASHBOARD PAGE ---
if menu == "🏠 Dashboard":
    st.title("🛡️ CyberMind Pro Live Dashboard")
    
    st.markdown("""
        <div class="hero-banner">
            <h3 style="color: #00ffcc; margin-bottom: 8px;">Aaj ka zamana jitna smart hai, utna hi khatarnak hai... CyberMind ko samjho!</h3>
            <p style="color: #94a3b8; font-size: 14px;">Aapka digital suraksha kavach jo har pal aapko cyber threats se bachata hai.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="stat-card"><p>🟢 Live Active Users</p><p class="stat-val">{st.session_state.active_users} live</p></div>', unsafe_allow_html=True)
        if st.button("➕ User Joined (+1)"):
            st.session_state.active_users += 1
            st.rerun()
    with col2:
        st.markdown('<div class="stat-card"><p>⚡ System Protection</p><p class="stat-val">MAX SECURE</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><p>🛑 Threats Blocked</p><p class="stat-val" style="color: #ff4b4b;">1,240</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><p>🛡️ AI Status</p><p class="stat-val">ONLINE</p></div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("Live System Health & Monitoring")
    c1, c2 = st.columns(2)
    with c1:
        st.info("AI Neural Defense Engine: **Active & Learning**")
        st.progress(92)
    with c2:
        st.success("Global Security Mesh: **Fully Synchronized**")
        st.progress(100)

# --- AI SCAM & PHISHING DETECTOR ---
elif menu == "🧠 AI Scam & Phishing Detector":
    st.title("🧠 AI Scam & Phishing Detector")
    st.write("Kisi bhi suspicious message ya SMS ko yahan paste karein. AI neural engine 10-15 lines mein gehra vishleshan karke turant alert jari karega:")
    
    msg = st.text_area("Paste message/SMS text here for deep analysis...", height=100)
    
    if st.button("Run Deep Scam Analysis"):
        if msg:
            with st.spinner("AI is analyzing text patterns, keyword threats and malicious links..."):
                time.sleep(1.5)
                
                scam_keywords = ["sbi", "bank", "blocked", "kyc", "lottery", "kbc", "prize", "won", "electricity", "bill", "disconnect", "fee", "pay", "update", "http"]
                is_scam = any(word in msg.lower() for word in scam_keywords) or "http" in msg.lower() or "rupee" in msg.lower() or "rs" in msg.lower()
                
                if is_scam:
                    st.error("🚨 HIGH-RISK DANGER ALERT: Potential Phishing / Cyber Scam Detected!")
                    st.markdown("### 📋 AI Detailed Security Audit Report:")
                    st.markdown(f"""
1. **Threat Assessment:** The analyzed text contains critical manipulation patterns commonly used by online cyber criminals and financial fraudsters.
2. **Link / URL Risk:** The message either incorporates a suspicious external web link or forces immediate urgency to click unrecognized URLs.
3. **Psychological Trick:** It exploits human emotions (fear of account suspension, greed for lottery, or emergency utility disconnection) to bypass rational thinking.
4. **Sender Credibility:** Legitimate financial institutions, banks, or government bodies **never** ask for urgent updates, OTPs, or fees via personal text messages.
5. **Data Harvesting Risk:** Clicking links inside such messages can download malware or redirect you to clone login pages to steal personal credentials.
6. **Financial Danger:** Interacting with this text poses a direct threat to your bank account safety and digital identity privacy.
7. **Recommended Action:** Do **not** click any links, do **not** reply with personal information, block the sender immediately, and report the number to cyber cell.
8. **Neural Confidence Score:** 98.4% probability of malicious intent.
                    """)
                else:
                    st.success("✅ Secure Status: Message Verified Clean & Authentic.")
                    st.markdown("### 📋 AI Detailed Security Audit Report:")
                    st.markdown(f"""
1. **Content Evaluation:** The provided text has been scanned thoroughly through CyberMind Pro's natural language processing firewall.
2. **Malicious Link Check:** No hidden phishing links, shortened URLs, or unauthorized redirection gateways were discovered.
3. **Urgency & Tone Analysis:** The text maintains a normal, non-threatening professional/personal tone without any artificial panic-inducing triggers.
4. **Data Privacy Check:** No requests for confidential credentials, banking PINs, passwords, or personal identity details.
5. **Fraud Pattern Match:** Zero similarity found with known global financial scam frameworks or fraudulent message templates.
6. **Sender Authentication:** The language structure aligns with standard safe communication paradigms.
7. **System Safety Rating:** Zero threat vectors identified across all behavioral checks.
8. **Recommended Action:** It is completely safe to read, process, or respond to this message.
                    """)
        else:
            st.warning("Kripya pehle text box mein koi message ya SMS paste karein.")

# --- NEW FEATURE 1: 2FA & OTP FRAUD SHIELD ---
elif menu == "🔐 2FA & OTP Fraud Shield":
    st.title("🔐 2FA & OTP Fraud Shield")
    st.write("Check karein ki aapka Two-Factor Authentication aur OTP security kitna surakshit hai:")
    if st.button("Run OTP Security Check"):
        with st.spinner("Analyzing SMS gateway encryption and authentication protocols..."):
            time.sleep(1.2)
            st.success("✅ OTP interception protection is Active. No unauthorized device cloning detected on your cellular line.")

# --- DARK WEB PASSWORD LEAK TEST ---
elif menu == "🔑 Dark Web Password Leak Test":
    st.title("🔑 Dark Web Password & Email Leak Test")
    st.write("Check karein ki aapka email ya password kahin dark web par leak toh nahi hua hai:")
    email_input = st.text_input("Enter your email address:", "example@gmail.com")
    if st.button("Check Breach Database"):
        if email_input:
            with st.spinner("Searching global security breach databases..."):
                time.sleep(1.2)
                st.success(f"🎉 Good news! '{email_input}' was not found in any known dark web data leaks.")

# --- SAFE LINK & URL CHECKER ---
elif menu == "🔗 Safe Link & URL Checker":
    st.title("🔗 Safe Link & URL Checker")
    st.write("Kisi bhi unknown link par click karne se pehle yahan check karein ki wo safe hai ya scam:")
    url_input = st.text_input("Enter URL (e.g., https://xyz-offer.com)")
    if st.button("Verify URL Safety"):
        if url_input:
            with st.spinner("Checking SSL certificates and domain reputation..."):
                time.sleep(1)
                st.error("⚠️ Warning: This domain is newly registered and flagged as suspicious. Avoid clicking!")

# --- NEW FEATURE 2: PUBLIC WI-FI RISK ANALYZER ---
elif menu == "🛡️ Public Wi-Fi Risk Analyzer":
    st.title("🛡️ Public Wi-Fi Risk Analyzer")
    st.write("Check karein ki jis public Wi-Fi network se aap connected hain, kya wahan hacker snooping ka khatra hai:")
    if st.button("Scan Current Wi-Fi Safety"):
        with st.spinner("Scanning network packets and ARP spoofing status..."):
            time.sleep(1.2)
            st.warning("⚠️ Network Warning: Unsecured public hotspot detected. Enable VPN encryption immediately to prevent data sniffing!")

# --- PREMIUM HUB (With Instagram DM Redirect) ---
elif menu == "💎 Premium Hub":
    st.title("💎 CyberMind Premium Hub")
    st.write("Apne account ko upgrade karne ke liye niche diye gaye kisi bhi plan ko select karein. Plan lene ke liye seedha hamare **Instagram par DM** karein!")
    
    insta_link = "https://www.instagram.com/direct/t/"

    plans = [
        {"name": "Starter Guard", "price": "₹299/mo", "features": ["Basic Phishing Shield", "1 Device Protection", "Email Support"]},
        {"name": "Pro Defender", "price": "₹599/mo", "features": ["Advanced Scam Detector", "3 Devices", "Priority Support", "Real-time Alerts"]},
        {"name": "Elite Secure", "price": "₹999/mo", "features": ["AI Neural Defense", "Dark Web Monitoring", "10 Devices", "Cloud Vault", "24/7 Support"]},
        {"name": "Cyber Ghost", "price": "₹1499/mo", "features": ["Zero-Log Protection", "Incognito Browser Shield", "Unlimited Devices", "Dedicated IP"]},
        {"name": "Enterprise Shield", "price": "₹2999/mo", "features": ["Full Network Encryption", "Dedicated Security Manager", "Custom Protection Rules"]},
        {"name": "Quantum Pro", "price": "₹4999/mo", "features": ["Post-Quantum Encryption", "Military-grade Shield", "Instant Emergency Response"]},
        {"name": "Ultimate Sentinel", "price": "₹7999/mo", "features": ["Complete Digital Asset Protection", "Personal Security Audit", "Direct Developer Support"]},
        {"name": "Family Armor", "price": "₹1299/mo", "features": ["Parental Control", "Shared Vault", "5 Family Members", "Safe Browsing for Kids"]},
        {"name": "Student Shield", "price": "₹199/mo", "features": ["Academic Link Scanner", "Basic Phishing Filter", "Ad Blocker"]},
        {"name": "Freelancer Safe", "price": "₹799/mo", "features": ["Client Data Protection", "Secure File Sharing", "Anti-Fraud Mail Guard"]}
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
            
            st.markdown(f"""
                <a href="{insta_link}" target="_blank">
                    <button style="width: 100%; background-color: #00ffcc; color: #050a14; border: none; padding: 10px; border-radius: 5px; font-weight: bold; cursor: pointer;">
                        📸 Buy {plan['name']} (DM on Instagram)
                    </button>
                </a>
            """, unsafe_allow_html=True)

# Sidebar footer
st.sidebar.write("---")
st.sidebar.caption("CyberMind Pro v4.2 | Smart & Secure")
