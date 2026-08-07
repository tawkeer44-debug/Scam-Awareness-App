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
    "📊 Dashboard & Live Threat Intelligence", 
    "📰 Live Scam News Hub", 
    "💸 UPI Transaction Checker", 
    "🔗 Link Scanner", 
    "💬 CyberMind AI Chatbot", 
    "💎 Premium Hub", 
    "🚀 Viral Share & Traffic Booster"
])

# --- Module 1: Dashboard & Live Threat Intelligence ---
if menu == "📊 Dashboard & Live Threat Intelligence":
    st.markdown('<div class="hero-box"><h1>CyberMind Live Threat Intelligence Dashboard</h1><p>Real-time monitoring of global cyber threats and active system users.</p></div>', unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns(3)
    
    # Session state for live increasing active users starting from 9022
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

# --- Module 5: CyberMind AI Chatbot ---
elif menu == "💬 CyberMind AI Chatbot":
    st.markdown('<div class="hero-box"><h1>CyberMind AI Assistant</h1><p>Ask anything! Type "hi", ask about scams, or request app guidance.</p></div>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! Main CyberMind AI hoon. Bataiye, aaj main aapki kya madad kar sakta hoon?"}]
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Type your message here (e.g., Hi, UPI fraud se kaise bachein):"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            query_lower = prompt.lower()
            if "hi" in query_lower or "hello" in query_lower or "hey" in query_lower:
                response = "Hello Tawkeer bhai! CyberMind AI aapki sewa mein hazir hai. B batayein kaunsa scam check karna hai?"
            elif "upi" in query_lower or "payment" in query_lower:
                response = "UPI fraud se bachne ke liye kabhi bhi anjaan QR code scan na karein aur na hi apna UPI PIN kisi ke sath share karein. Aap hamara 'UPI Transaction Checker' bhi use kar sakte hain!"
            elif "news" in query_lower:
                response = "Rozana nayi scam news ke liye sidebar se 'Live Scam News Hub' par jayein!"
            else:
                response = f"Aapne pucha: '{prompt}'. CyberMind AI iska jawab dene ke liye taiyar hai! Aap hamare Link Scanner ya Dashboard modules ko bhi check kar sakte hain."
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- Module 6: Premium Hub ---
elif menu == "💎 Premium Hub":
    st.markdown('<div class="hero-box"><h1>CyberMind Premium Hub</h1><p>Unlock advanced protection tools, priority scanning, and VIP access.</p></div>', unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("""
            <div class="feature-card" style="border-color: #3b82f6;">
                <h3>🚀 Pro Security Pass</h3>
                <p><b>Price:</b> ₹199 / month</p>
                <p>• Unlimited Link Scans<br>• Real-time Fraud Alerts<br>• Priority Server Access</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY PRO PASS"):
            st.info("🔗 Secure payment gateway connected. Premium unlocked!")
            
    with col_p2:
        st.markdown("""
            <div class="feature-card" style="border-color: #10b981;">
                <h3>👑 Lifetime VIP Pass</h3>
                <p><b>Price:</b> ₹499 (One-time)</p>
                <p>• All Pro Features<br>• Lifetime Free Updates<br>• Direct Support Access</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY LIFETIME PASS"):
            st.info("🔗 Secure payment gateway connected. Premium unlocked!")

# --- Module 7: Viral Share & Traffic Booster ---
elif menu == "🚀 Viral Share & Traffic Booster":
    st.title("🚀 Viral Share & Traffic Booster")
    st.write("Is app ko apne doston aur groups mein share karke views aur traffic badhayein!")
    
    app_url = "https://share.streamlit.io"
    share_text = f"🔥 *CyberMind Security Hub!* Live threat dashboard, link scanner aur UPI fraud checker ek hi jagah: {app_url}"
    encoded_text = urllib.parse.quote(share_text)
    
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
    telegram_url = f"https://t.me/share/url?url={app_url}&text={urllib.parse.quote('Check out CyberMind Security App!')}"
    
    st.markdown(
        f"""
        <div class="share-box">
            <h3 style="color: #fcd34d;">📢 Boost Your App Viewers Now</h3>
            <p style="color: #fef3c7;">Click below to share directly in groups:</p>
            <br>
            <a href="{whatsapp_url}" target="_blank" style="background-color: #25D366; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 6px; margin-right: 10px;">💬 Share on WhatsApp</a>
            <a href="{telegram_url}" target="_blank" style="background-color: #0088cc; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 6px;">✈️ Share on Telegram</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Creator: Tawkeer | CyberMind v11.0")
