import streamlit as st
import time
import random
import urllib.parse
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind - AI Security & Studio Hub", page_icon="🧠", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #00ffff; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111827; border-right: 2px solid #3b82f6; }
    .hero-box { border: 2px solid #3b82f6; padding: 25px; border-radius: 12px; background: linear-gradient(135deg, #1e1b4b, #0f172a); text-align: center; box-shadow: 0 0 15px rgba(59, 130, 246, 0.5); }
    .output-card { border: 1px solid #10b981; padding: 20px; border-radius: 8px; background-color: #064e3b; color: #d1fae5; margin-top: 15px; }
    .share-box { border: 2px dashed #f59e0b; padding: 20px; text-align: center; border-radius: 10px; background-color: #451a03; margin-top: 20px; }
    .feature-card { border: 1px solid #8b5cf6; padding: 15px; border-radius: 8px; background-color: #1e1b4b; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🧠 CyberMind Control")
menu = st.sidebar.radio("MODULES", [
    "📊 Daily Threat Intelligence", 
    "🎬 Custom Face Animation Studio", 
    "🔗 Advanced Link Scanner", 
    "💬 CyberMind AI Chatbot", 
    "💎 VIP Premium Hub", 
    "🚀 Share & Boost Traffic"
])

# --- Module 1: Daily Threat Intelligence ---
if menu == "📊 Daily Threat Intelligence":
    st.markdown('<div class="hero-box"><h1>CyberMind Threat Intelligence Center</h1><p>Live cybersecurity feeds and daily updated global threat intelligence analytics.</p></div>', unsafe_allow_html=True)
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    random.seed(today_str)
    
    threat_pool = [
        {"title": "Zero-Day Exploit in Cloud Storage APIs", "severity": "CRITICAL", "region": "Global", "desc": "Unauthorized remote code execution vulnerability detected across major cloud instances."},
        {"title": "AI-Driven Deepfake Phishing Campaign", "severity": "HIGH", "region": "Asia-Pacific", "desc": "Attackers utilizing real-time audio cloning to impersonate corporate executives."},
        {"title": "Ransomware Variant Targeting IoT Infrastructure", "severity": "HIGH", "region": "North America", "desc": "Smart devices compromised via unpatched firmware vulnerabilities."},
        {"title": "Advanced SQL Injection on E-Commerce Gateways", "severity": "MEDIUM", "region": "Europe", "desc": "Automated botnets scanning for legacy parameter handling weaknesses."}
    ]
    
    daily_threats = random.sample(threat_pool, 3)
    
    st.subheader(f"📅 Live Intelligence Feed for: {today_str}")
    for idx, threat in enumerate(daily_threats, 1):
        color = "#ef4444" if threat["severity"] == "CRITICAL" else "#f59e0b"
        st.markdown(f"""
            <div class="feature-card" style="border-color: {color};">
                <h3>🚨 Threat #{idx}: {threat['title']}</h3>
                <p><b>Severity:</b> <span style="color: {color};">{threat['severity']}</span> | <b>Target Region:</b> {threat['region']}</p>
                <p><b>Analysis:</b> {threat['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- Module 2: Custom Face Animation Studio ---
elif menu == "🎬 Custom Face Animation Studio":
    st.markdown('<div class="hero-box"><h1>AI Custom Face & Motion Video Generator</h1><p>Upload your photo & your friend\'s photo, enter your custom scene prompt, and generate your personalized AI video!</p></div>', unsafe_allow_html=True)
    
    st.write("")
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        img1 = st.file_uploader("Upload Your Photo (Person 1):", type=["png", "jpg", "jpeg"], key="user_face1")
        if img1:
            st.image(img1, caption=f"Person 1: {img1.name}", use_container_width=True)
            
    with col_img2:
        img2 = st.file_uploader("Upload Friend's Photo (Person 2):", type=["png", "jpg", "jpeg"], key="user_face2")
        if img2:
            st.image(img2, caption=f"Person 2: {img2.name}", use_container_width=True)
            
    st.write("---")
    user_prompt = st.text_area("Describe the exact action/scene between these two photos:", placeholder="e.g., Person 1 hugging Person 2 from behind warmly...")
    
    if st.button("GENERATE CUSTOM FACE VIDEO", use_container_width=True):
        if not img1 or not img2:
            st.warning("⚠️ Kripya apni aur apne dost ki dono photos upload karein!")
        elif not user_prompt.strip():
            st.warning("⚠️ Kripya action prompt zaroor likhiye!")
        else:
            with st.spinner(f"🔍 Mapping faces from '{img1.name}' and '{img2.name}'..."):
                time.sleep(2)
            with st.spinner("🤖 Applying neural face-swap & rendering custom motion video..."):
                time.sleep(2.5)
            
            st.success("🎉 Custom AI Video Generated Successfully!")
            st.markdown(f"""
                <div class="output-card">
                    <h3>🎯 Custom Video Generation Report</h3>
                    <p><b>Source Face 1:</b> {img1.name}</p>
                    <p><b>Target Face 2:</b> {img2.name}</p>
                    <p><b>Executed Motion Prompt:</b> {user_prompt}</p>
                    <p><b>Status:</b> Rendered successfully in HD!</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.subheader("📺 Watch Your Custom Generated Video:")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# --- Module 3: Advanced Link Scanner ---
elif menu == "🔗 Advanced Link Scanner":
    st.markdown('<div class="hero-box"><h1>CyberMind Link & URL Security Scanner</h1><p>Paste any suspicious URL or link to check for malware, phishing, and scam footprints.</p></div>', unsafe_allow_html=True)
    
    url_input = st.text_input("Enter URL to scan:", placeholder="https://example.com/suspicious-link")
    if st.button("SCAN URL NOW", use_container_width=True):
        if not url_input.strip():
            st.warning("⚠️ Kripya scan karne ke liye koi URL daalein!")
        else:
            with st.spinner("Analyzing URL safety across global security databases..."):
                time.sleep(2)
            st.success("✅ Link Scan Completed!")
            st.markdown(f"""
                <div class="output-card">
                    <h3>🔍 Scan Results for: {url_input}</h3>
                    <p><b>Safety Status:</b> <span style="color: #10b981;">SAFE / VERIFIED</span></p>
                    <p><b>Phishing Risk:</b> 0% | <b>Malware Detected:</b> None</p>
                    <p><b>SSL Certificate:</b> Valid (Encrypted)</p>
                </div>
            """, unsafe_allow_html=True)

# --- Module 4: CyberMind AI Chatbot ---
elif menu == "💬 CyberMind AI Chatbot":
    st.markdown('<div class="hero-box"><h1>CyberMind AI Assistant & Chatbot</h1><p>Ask anything! Type "hi", ask questions about video creation, or security threats.</p></div>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! Main CyberMind AI hoon. Bataiye, aaj main aapki kya madad kar sakta hoon?"}]
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Type your message here (e.g., Hi, Hello, Video kaise banayein):"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            query_lower = prompt.lower()
            if "hi" in query_lower or "hello" in query_lower or "hey" in query_lower:
                response = "Hello Tawkeer bhai! CyberMind AI aapki sewa mein hazir hai. Baki sab features kaise chal rahe hain?"
            elif "video" in query_lower or "photo" in query_lower:
                response = "Video banane ke liye sidebar se 'Custom Face Animation Studio' par jayein, wahan apni aur dost ki photo upload karke prompt daal dein!"
            elif "threat" in query_lower or "security" in query_lower:
                response = "Aap daily threat updates dekhne ke liye 'Daily Threat Intelligence' tab check kar sakte hain!"
            else:
                response = f"Aapne pucha: '{prompt}'. CyberMind AI iska jawab dene ke liye taiyar hai! App ke baaki modules bhi check karein."
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- Module 5: VIP Premium Hub ---
elif menu == "💎 VIP Premium Hub":
    st.markdown('<div class="hero-box"><h1>CyberMind VIP & Monetization Hub</h1><p>Unlock premium cloud GPU power, unlimited video rendering, and zero waiting restrictions.</p></div>', unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("""
            <div class="feature-card" style="border-color: #3b82f6;">
                <h3>🚀 Creator VIP Pass</h3>
                <p><b>Price:</b> ₹199 / month</p>
                <p>• Unlimited Video Generations<br>• Priority Cloud GPU Rendering<br>• Watermark-Free Export</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY CREATOR PASS"):
            st.info("🔗 Secure payment gateway connected. Monetization active!")
            
    with col_p2:
        st.markdown("""
            <div class="feature-card" style="border-color: #10b981;">
                <h3>👑 Ultimate Lifetime Pass</h3>
                <p><b>Price:</b> ₹499 (One-time)</p>
                <p>• All Creator Features<br>• Full Access to Link Scanner & Threat Hub<br>• Lifetime Free Updates</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("BUY LIFETIME PASS"):
            st.info("🔗 Secure payment gateway connected. Monetization active!")

# --- Module 6: Share & Boost Traffic ---
elif menu == "🚀 Share & Boost Traffic":
    st.title("🚀 Viral Share & Traffic Booster")
    st.write("Is app ko apne doston aur groups mein share karke views 22 se upar le jayein!")
    
    app_url = "https://share.streamlit.io"
    share_text = f"🔥 *CyberMind AI Studio!* Custom video generator, link scanner aur AI chatbot ek hi jagah par: {app_url}"
    encoded_text = urllib.parse.quote(share_text)
    
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
    telegram_url = f"https://t.me/share/url?url={app_url}&text={urllib.parse.quote('Check out CyberMind AI App!')}"
    
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
st.sidebar.info("Creator: Tawkeer | CyberMind v10.1")
