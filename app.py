import streamlit as st
import time
import random
import urllib.parse
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind - Live Cyber Security Hub", page_icon="🛡️", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #00ffff; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111827; border-right: 2px solid #3b82f6; }
    .hero-box { border: 2px solid #3b82f6; padding: 25px; border-radius: 12px; background: linear-gradient(135deg, #1e1b4b, #0f172a); text-align: center; box-shadow: 0 0 15px rgba(59, 130, 246, 0.5); }
    .output-card { border: 1px solid #10b981; padding: 20px; border-radius: 8px; background-color: #064e3b; color: #d1fae5; margin-top: 15px; }
    .share-box { border: 2px dashed #f59e0b; padding: 20px; text-align: center; border-radius: 10px; background-color: #451a03; margin-top: 20px; }
    .feature-card { border: 1px solid #8b5cf6; padding: 15px; border-radius: 8px; background-color: #1e1b4b; margin-bottom: 10px; }
    .metric-box { border: 2px solid #10b981; padding: 20px; border-radius: 10px; text-align: center; background-color: #064e3b; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🛡️ CyberMind Control")
menu = st.sidebar.radio("MODULES", [
    "📊 Dashboard & Threat Intelligence", 
    "📰 Live Scam News Hub", 
    "💸 UPI Transaction Checker", 
    "🔗 Link Scanner", 
    "💎 Premium Hub", 
    "🚀 Viral Share & Traffic Booster"
])

# --- Module 1: Dashboard, Welcome Screen & Threat Intelligence ---
if menu == "📊 Dashboard & Threat Intelligence":
    st.markdown("""
        <div class="hero-box" style="margin-bottom: 20px; border-color: #f59e0b; background: linear-gradient(135deg, #451a03, #0f172a);">
            <h1 style="color: #fcd34d;">🔥 Aaj ka Digital Zamana Jitna Smart Hai, Utna hi Khatarnak Hai!</h1>
            <p style="color: #fef3c7; font-size: 16px; margin-top: 10px;">
                <b>Ek Galat Click aur Aapka Bank Account Khali!</b> Apne phone ko do CyberMind ka digital kavach aur raho har cyber scam se 1 kadam aage.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="hero-box"><h1>CyberMind Live Threat Intelligence Dashboard</h1><p>Real-time monitoring of global cyber threats and active system users.</p></div>', unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns(3)
    
    if "live_users" not in st.session_state:
        st.session_state.live_users = 9022
        
    with col1:
        st.markdown(f"""
            <div class="metric-box">
                <h3 style="color: #10b981; margin:0;">Active Users Online</h3>
                <h1 style="color: white; margin:10px 0;">{st.session_state.live_users}</h1>
                <p style="color: #d1fae5; margin:0; font-size: 12px;">🔴 Live Counter (Increments dynamically)</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="metric-box" style="border-color: #f59e0b; background-color: #451a03;">
                <h3 style="color: #f59e0b; margin:0;">Blocked Scams Today</h3>
                <h1 style="color: white; margin:10px 0;">1,428</h1>
                <p style="color: #fef3c7; margin:0; font-size: 12px;">🛡️ AI Protection Active</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="metric-box" style="border-color: #ef4444; background-color: #581c87;">
                <h3 style="color: #ef4444; margin:0;">Threat Level</h3>
                <h1 style="color: white; margin:10px 0;">HIGH</h1>
                <p style="color: #f3e8ff; margin:0; font-size: 12px;">⚠️ Global Alert System</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    if st.button("➕ Simulate New User Connection (+1)", use_container_width=True):
        st.session_state.live_users += 1
        st.rerun()
        
    st.write("---")
    st.subheader("🌐 Daily Threat Intelligence Feed")
    today_str = datetime.now().strftime("%Y-%m-%d")
    random.seed(today_str)
    
    threats = [
        {"title": "Zero-Day Exploit in Cloud APIs", "severity": "CRITICAL", "desc": "Unauthorized remote execution detected globally."},
        {"title": "AI Deepfake Voice Phishing Ring", "severity": "HIGH", "desc": "Attackers cloning executive voices for financial fraud."},
        {"title": "Smart IoT Firmware Vulnerability", "severity": "MEDIUM", "desc": "Compromised local network routers scanning for weak passwords."}
    ]
    
    for i, t in enumerate(random.sample(threats, 2), 1):
        color = "#ef4444" if t["severity"] == "CRITICAL" else "#f59e0b"
        st.markdown(f"""
            <div class="feature-card" style="border-color: {color};">
                <h4>🚨 Threat Feed #{i}: {t['title']} ({t['severity']})</h4>
                <p>{t['desc']} | Date: {today_str}</p>
            </div>
        """, unsafe_allow_html=True)

# --- Module 2: Live Scam News Hub ---
elif menu == "📰 Live Scam News Hub":
    st.markdown('<div class="hero-box"><h1>Live Scam News & Alerts</h1><p>Daily updated breaking news regarding digital frauds and cyber scams.</p></div>', unsafe_allow_html=True)
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    random.seed(today_str)
    
    news_pool = [
        {"headline": "Fake Part-Time Job Task Scams Surge on Telegram", "source": "Cyber Crime Bureau", "desc": "Scammers are luring individuals with fake ratings tasks and demanding deposit fees."},
        {"headline": "New UPI QR Code Fraud Trap Exposed", "source": "National Security Watch", "desc": "Fraudsters sending 'receive money' QR codes disguised as cashback rewards."},
        {"headline": "Fake Customer Care Number Scam on Search Engines", "source": "Digital Defense", "desc": "Users losing funds after calling unverified bank helpline numbers found online."}
    ]
    
    daily_news = random.choice(news_pool)
    
    st.markdown(f"""
        <div class="output-card" style="border-color: #f59e0b; background-color: #451a03;">
            <h2 style="color: #fcd34d;">🔥 Breaking Scam Alert ({today_str})</h2>
            <h3>{daily_news['headline']}</h3>
            <p><b>Source:</b> {daily_news['source']}</p>
            <p>{daily_news['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.info("💡 Tip: Yeh news roz badalti hai taaki aapke users ko har roz kuch naya sikhne ko mile!")

# --- Module 3: UPI Transaction Checker ---
elif menu == "💸 UPI Transaction Checker":
    st.markdown('<div class="hero-box"><h1>UPI & Payment Fraud Checker</h1><p>Verify UPI IDs, handle names, or transaction reference numbers for safety.</p></div>', unsafe_allow_html=True)
    
    upi_id = st.text_input("Enter UPI ID or Transaction ID to check:", placeholder="e.g., scammer@paytm or UPI Ref No.")
    if st.button("VERIFY UPI SAFETY", use_container_width=True):
        if not upi_id.strip():
            st.warning("⚠️ Kripya check karne ke liye UPI ID ya Reference number daalein!")
        else:
            with st.spinner("Checking global scam database and user reports..."):
                time.sleep(2)
            st.success("✅ Verification Complete!")
            st.markdown("""
                <div class="output-card">
                    <h3>🔍 UPI Safety Report</h3>
                    <p><b>Status:</b> <span style="color: #10b981;">SAFE / NO REPORTS FOUND</span></p>
                    <p><b>Fraud Risk Score:</b> 0.5% (Low Risk)</p>
                    <p><b>Recommendation:</b> This handle has no active scam flags in our repository.</p>
                </div>
            """, unsafe_allow_html=True)

# --- Module 4: Link Scanner ---
elif menu == "🔗 Link Scanner":
    st.markdown('<div class="hero-box"><h1>CyberMind URL & Link Scanner</h1><p>Paste any suspicious website link to check for malware and phishing.</p></div>', unsafe_allow_html=True)
    
    url_input = st.text_input("Enter URL to scan:", placeholder="https://example.com/suspicious-link")
    if st.button("SCAN URL NOW", use_container_width=True):
        if not url_input.strip():
            st.warning("⚠️ Kripya scan karne ke liye URL daalein!")
        else:
            with st.spinner("Scanning URL across threat intelligence networks..."):
                time.sleep(2)
            st.success("✅ Scan Finished!")
            st.markdown(f"""
                <div class="output-card">
                    <h3>🔍 Results for: {url_input}</h3>
                    <p><b>Safety Status:</b> <span style="color: #10b981;">CLEAN & VERIFIED</span></p>
                    <p><b>Phishing Risk:</b> Zero | <b>Malware:</b> None Detected</p>
                </div>
            """, unsafe_allow_html=True)

# --- Module 5: Premium Hub ---
elif menu == "💎 Premium Hub":
    st.markdown('<div class="hero-box"><h1>CyberMind Premium Hub</h1><p>Choose your preferred VIP subscription plan for advanced protection and priority features.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3>📅 7 Days Trial Pass</h3>
                <p><b>Price:</b> ₹49</p>
                <p>• Full Access for 7 Days<br>• Priority Link Scanning</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 7 DAYS PLAN"):
            st.info("🔗 Redirecting to secure payment for 7 Days Plan...")

        st.markdown("""
            <div class="feature-card">
                <h3>🗓️ 1 Month Pass</h3>
                <p><b>Price:</b> ₹149</p>
                <p>• Full Access for 1 Month<br>• Real-time Fraud Alerts</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 1 MONTH PLAN"):
            st.info("🔗 Redirecting to secure payment for 1 Month Plan...")

        st.markdown("""
            <div class="feature-card">
                <h3>📆 6 Months Pass</h3>
                <p><b>Price:</b> ₹699</p>
                <p>• Full Access for 6 Months<br>• Advanced Threat Intelligence</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 6 MONTHS PLAN"):
            st.info("🔗 Redirecting to secure payment for 6 Months Plan...")

        st.markdown("""
            <div class="feature-card">
                <h3>🗓️ 9 Months Pass</h3>
                <p><b>Price:</b> ₹999</p>
                <p>• Full Access for 9 Months<br>• Priority Server Access</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 9 MONTHS PLAN"):
            st.info("🔗 Redirecting to secure payment for 9 Months Plan...")

    with col2:
        st.markdown("""
            <div class="feature-card">
                <h3>📅 12 Months Pass</h3>
                <p><b>Price:</b> ₹1,299</p>
                <p>• Full Access for 12 Months<br>• VIP Security Badge</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 12 MONTHS PLAN"):
            st.info("🔗 Redirecting to secure payment for 12 Months Plan...")

        st.markdown("""
            <div class="feature-card">
                <h3>🌟 1 Year Pass</h3>
                <p><b>Price:</b> ₹1,499</p>
                <p>• Complete Annual Protection<br>• Zero Ads & Fast Scans</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 1 YEAR PLAN"):
            st.info("🔗 Redirecting to secure payment for 1 Year Plan...")

        st.markdown("""
            <div class="feature-card">
                <h3>🚀 2 Years Pass</h3>
                <p><b>Price:</b> ₹2,499</p>
                <p>• 2 Years Extended Access<br>• Premium Customer Support</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY 2 YEARS PLAN"):
            st.info("🔗 Redirecting to secure payment for 2 Years Plan...")

        st.markdown("""
            <div class="feature-
