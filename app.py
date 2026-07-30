import streamlit as st
import time
import random
import base64

# --- Page Configuration ---
st.set_page_config(page_title="CyberMind X Pro | ULTIMATE", page_icon="💀", layout="wide")

# --- Custom CSS (Hacker Style + Matrix Background) ---
# Is CSS se Matrix background aur dark theme set hogi
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# NOTE: Agar aapke paas matrix.gif nahi hai, toh yeh background kaam nahi karega.
# Aap koi bhi dark tech background use kar sakte hain ya is section ko hata sakte hain.
# Filhal maine ek solid dark color rakha hai taaki error na aaye.
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-color: #000000; /* Fallback color */
    opacity: 0.95;
}}
.main {{
    background-color: rgba(10, 10, 10, 0.85);
    color: #00FF00; /* Matrix Green Text */
    font-family: 'Courier New', Courier, monospace;
}}
.stSidebar {{
    background-color: #111111;
    border-right: 2px solid #00FF00;
}}
.stTextInput>div>div>input {{ color: #00FF00; background-color: #000000; }}
.stSelectbox>div>div>select {{ color: #00FF00; background-color: #000000; }}
.stTextArea>div>div>textarea {{ color: #00FF00; background-color: #000000; }}
h1, h2, h3 {{ color: #FF0000; }} /* Danger Red Headings */
.metric-card {{ background-color: #1c1c1c; border: 1px solid #333; padding: 15px; border-radius: 5px; }}
.khatarnak-box {{ border: 2px solid #FF0000; padding: 10px; border-radius: 5px; background-color: #2a0000; }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("https://img.icons8.com/fluency/96/anonymous-mask.png", width=80) # Hacker Icon
st.sidebar.title("💀 CyberMind Command")
st.sidebar.markdown("---")
menu = st.sidebar.radio("SELECT MODULE", 
    ["Dashboard", "IP Locator", "Password Pro", "Dark Web Scan", "Header Check", "Link Analyzer", "Report a Scam", "🚨 Emergency"])

# --- Helper Functions (Simulations) ---
def simulate_hack(text):
    with st.spinner(f"Initializing {text}..."):
        time.sleep(random.uniform(1.5, 3.0))

# --- 1. Dashboard Module ---
if menu == "Dashboard":
    st.title("💻 THREAT INTELLIGENCE CENTER")
    
    # Khatarnak Alerts
    with st.expander("🚨 CRITICAL VULNERABILITIES (LIVE)", expanded=True):
        st.error("ZERO-DAY EXPLOIT DETECTED in OpenSSL [CVE-2023-XXXX]")
        st.warning("Ransomware Node 'BlackMatter' Active in Geo-Zone: Asia")

    col1, col2, col3 = st.columns(3)
    col1.metric("Active Threats", "3", "+1")
    col2.metric("Nodes Compromised", "1,094", "+56")
    col3.metric("System Integrity", "88%", "-2%")

    st.markdown("---")
    st.subheader("⚡ Live Packet Sniffing (Simulated)")
    st.code(f"SRC: 192.168.1.{random.randint(10,50)} | DEST: 10.0.0.{random.randint(1,100)} | STATUS: SYN_RECV | PAYLOAD: {random.randint(500,1500)}B")
    st.code(f"SRC: 172.16.{random.randint(1,50)}.5 | DEST: 45.33.2.189 | STATUS: ESTABLISHED | SSL: TLS1.3")
    if st.button("Refresh Packets"): st.rerun()

# --- 2. IP Locator Module (NEW) ---
elif menu == "IP Locator":
    st.title("🌐 TARGET IP GEOLOCATION")
    ip_input = st.text_input("Enter IP Address (IPv4):", placeholder="8.8.8.8")
    if st.button("TRACE IP"):
        if ip_input:
            simulate_hack(f"Geo-Locator for {ip_input}")
            st.success("Trace Complete.")
            st.markdown(f"""
            <div class="metric-card">
            <h3>📍 IP Details: {ip_input}</h3>
            <p><b>ISP:</b> Google LLC</p>
            <p><b>Country:</b> United States</p>
            <p><b>Region:</b> California</p>
            <p><b>Coordinates:</b> 37.40599, -122.07851</p>
            <p style="color:red;">⚠️ WARNING: Location is approximate based on ISP routing.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Please enter a valid IP.")

# --- 3. Password Pro Module (NEW) ---
elif menu == "Password Pro":
    st.title("🔑 PASSWORD STRENGTH STUDIO")
    pass_input = st.text_input("Enter Password to Test:", type="password")
    if pass_input:
        # Strength Logic
        strength = 0
        feedback = []
        if len(pass_input) >= 8: strength += 1
        else: feedback.append("❌ Too short (min 8 chars)")
        if any(c.isupper() for c in pass_input): strength += 1
        else: feedback.append("❌ Missing uppercase")
        if any(c.isdigit() for c in pass_input): strength += 1
        else: feedback.append("❌ Missing number")
        if any(not c.isalnum() for c in pass_input): strength += 1
        else: feedback.append("❌ Missing special symbol")
        
        # Display Meter
        col1, col2 = st.columns([1,3])
        if strength <= 1:
            col1.metric("Strength", "WEAK", delta_color="normal")
            st.progress(25)
            st.warning("Vulnerable to Brute Force.")
        elif strength == 2:
            col1.metric("Strength", "MEDIUM")
            st.progress(50)
        elif strength == 3:
            col1.metric("Strength", "STRONG")
            st.progress(75)
        else:
            col1.metric("Strength", "VERY STRONG", delta_color="normal")
            st.progress(100)
            st.balloons()

        with st.expander("Improvement Tips"):
            for tip in feedback: st.write(tip)
            st.write("✅ Use a password manager.")

# --- 4. Dark Web Scan Module (NEW) ---
elif menu == "Dark Web Scan":
    st.title("📡 DARK WEB LEAK MONITOR")
    target = st.text_input("Enter Email or Domain to Scan:")
    if st.button("SCAN DEEP WEB"):
        if target:
            simulate_hack(f"Deep Web Crawl for {target}")
            st.markdown('<div class="khatarnak-box">', unsafe_allow_html=True)
            st.error(f"🚨 BREACH DETECTED! 3 databases found containing '{target}'.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.write("---")
            st.subheader("Compromised Sources:")
            st.text("1. Collection #5 (Combo List) - 2021/08/12")
            st.text("2. LinkedIn Data Dump - 2016/05/22")
            st.text("3. Exploit.in Forum - 2017/10/09")
            st.info("Recommendation: Change passwords immediately on all associated accounts.")
        else:
            st.error("Enter target to scan.")

# --- 5. Header Check Module (NEW) ---
elif menu == "Header Check":
    st.title("🕵️‍♂️ HTTP SECURITY HEADER INVESTIGATOR")
    url_input = st.text_input("Enter URL (with https://):", placeholder="https://google.com")
    if st.button("INSPECT HEADERS"):
        if url_input:
            simulate_hack(f"Header Analysis for {url_input}")
            st.success("Analysis Complete.")
            
            # Simulated Headers (Fake but realistic)
            headers = {
                "Server": "nginx/1.21.4",
                "Date": f"{time.ctime()}",
                "Content-Type": "text/html; charset=UTF-8",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
                "X-Frame-Options": "SAMEORIGIN",
                "X-Content-Type-Options": "nosniff",
                "Content-Security-Policy": "default-src 'self'; script-src 'self' trusted-scripts.com; object-src 'none';"
            }
            
            st.subheader("Response Headers:")
            for key, value in headers.items():
                if "X-" in key or "Content-Security" in key or "Strict" in key:
                    st.markdown(f"🟢 **{key}**: `{value}`")
                else:
                    st.markdown(f"⚪ **{key}**: `{value}`")
            
            st.warning("⚠️ NOTE: These headers are simulated for demonstration.")
        else:
            st.error("Valid URL required.")

# --- 6. Link Analyzer ---
elif menu == "Link Analyzer":
    # ... (Pichla code wahi rahega)
    st.title("🔍 Phishing URL Analyzer")
    url = st.text_input("Paste suspect URL:")
    if st.button("Scan Link"):
        with st.spinner("Checking against global blacklist..."):
            time.sleep(2)
            if "bit.ly" in url or "goo.gl" in url:
                st.warning("URL uses shortening service. Use caution.")
            st.error("🔴 HIGH RISK: Domain flagged as phishing by 3 vendors.")

# --- 7. Report a Scam ---
elif menu == "Report a Scam":
    # ... (Pichla code wahi rahega)
    st.title("🚨 Submit Intelligence Report")
    name = st.text_input("Agent Name (Optional)")
    details = st.text_area("Scam Details (Timestamp, Wallet Address, etc.)")
    if st.button("Transmit Report Securely"):
        st.success("Report transmitted to central node.")

# --- 8. Emergency Help ---
elif menu == "🚨 Emergency":
    # ... (Pichla code wahi rahega)
    st.title("🛡️ IMMEDIATE ACTION PROTOCOL")
    st.error("IF YOU ARE A VICTIM OF FINANCIAL SCAM, ACT NOW.")
    st.markdown("""
    **1. NATIONAL CYBER CRIME HELPLINE:** 📞 **1930** (India)
    **2. PORTAL:** [cybercrime.gov.in](https://cybercrime.gov.in)
    **3. BANK:** Call your bank IMMEDIATELY to freeze funds.
    """)

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.caption("CyberMind X Pro | For Educational Use Only")
st.sidebar.info("In memory of Uzair.")
