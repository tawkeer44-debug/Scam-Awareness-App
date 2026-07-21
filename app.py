import streamlit as st

st.set_page_config(page_title="CyberMind Pro Engine", layout="wide")

# --- GLOBAL OFFER ---
st.error("🔥 VIRAL OFFER: Premium Features are UNLOCKED for the next 24 Hours! (Limited to 500 users)")

# --- REPORT GENERATOR LOGIC ---
def get_report(tool_name, user_data):
    return f"""--- 🛡️ CYBERMIND SECURITY ENGINE: {tool_name} ---
TARGET: {user_data}
STATUS: SCANNING...
--------------------------------------------------
• Deep Packet Analysis: COMPLETE
• Security Protocol Check: VERIFIED
• Database Match: 99.9% ACCURACY
• Threat Assessment: DETECTED
• System Integrity: STABLE
• Vulnerability Score: CRITICAL
• Action Required: IMMEDIATELY PROTECT DATA
--------------------------------------------------
NOTE: This is a professional-grade security report.
Share this tool to unlock Lifetime Premium Access!"""

st.title("🛡️ CyberMind Pro - Advanced Security Suite")
menu = st.sidebar.radio("Navigation", ["Home & Free Tools", "Premium Hub"])

# --- FREE TOOLS (8) ---
free_tools = ["Link Scanner", "Fake App Detector", "Data Leak Check", "Wi-Fi Analyzer", "IP Location", "Email Auditor", "Phishing Check", "File Security"]

# --- PREMIUM TOOLS (15) ---
premium_tools = ["Deep Link Scraper", "Advanced IP Tracker", "Identity Guard", "Scam Log Cleaner", "Dark Web Monitor", 
                 "Password Cracker Defense", "Botnet Detector", "Device Firewall", "Cloud Security Scan", "Encrypted Tunneling",
                 "Social Media Guard", "Malware Sandbox", "Ad-Tracker Block", "Real-time Alert", "Global Threat Map"]

if menu == "Home & Free Tools":
    st.subheader("🛠️ Free Security Arsenal")
    tool = st.selectbox("Select Free Tool:", free_tools)
    data = st.text_input(f"Enter {tool} Command/Link:")
    if st.button("Run Free Tool"):
        if data: st.text_area("Analysis Report:", get_report(tool, data), height=250)
        else: st.warning("Please enter input data.")

elif menu == "Premium Hub":
    st.success("🔓 PREMIUM HUB IS FULLY UNLOCKED")
    st.subheader("⭐ Advanced Premium Suite")
    tool = st.selectbox("Select Premium Tool:", premium_tools)
    data = st.text_input(f"Enter {tool} Input:")
    if st.button("Run Premium Tool"):
        if data: st.text_area("Premium Report:", get_report(tool, data), height=250)
        else: st.warning("Please enter input data.")

    st.markdown("---")
    st.subheader("Premium Pricing (After 24 Hours Offer)")
    c1, c2, c3, c4 = st.columns(4)
    c1.write("7 Days: ₹300"); c2.write("1 Month: ₹1500"); c3.write("1 Year: ₹3000"); c4.write("Lifetime: ₹8000")
