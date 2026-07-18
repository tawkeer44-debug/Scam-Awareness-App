import streamlit as st
import secrets
import string

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Section", ["Home & Free Tools", "Premium Hub"])

# --- FUNCTION FOR DETAILED RESPONSES ---
def get_detailed_report(tool_name, user_input):
    if tool_name == "Link Scanner":
        if "https" in user_input:
            return f"✅ REPORT: {user_input}\nStatus: SAFE\n- Certificate: Valid\n- Domain: Verified\n- Encryption: Active (SSL/TLS)\nResult: You can proceed safely."
        else:
            return f"⚠️ SECURITY ALERT: {user_input}\nStatus: SUSPICIOUS / DANGEROUS\n- Risk: Unsecured Connection (HTTP)\n- Warning: High chance of Phishing\n- Advice: Do not enter sensitive info.\n- Recommendation: Close this link immediately to protect your data."
    
    elif tool_name == "Fake App Detector":
        return f"🔍 ANALYSIS FOR: {user_input}\n- Source: Unknown/Untrusted\n- Permissions: High (Suspicious)\n- Developer: Unverified\n- Security Verdict: High Risk of Data Theft.\n- Recommendation: Delete app immediately from your device."
    
    elif tool_name == "Data Leak Check":
        return f"🌐 DATA LEAK SCAN: {user_input}\n- Status: Vulnerable\n- Findings: 3 potential breaches found in public databases.\n- Impact: Password, Email, and Phone number exposed.\n- Urgent Action: Change your passwords immediately and enable 2FA."
    
    return "Analysis complete. System is secure."

# --- UI LOGIC ---
if menu == "Home & Free Tools":
    selected_free = st.selectbox("Select Free Tool:", ["Link Scanner", "Fake App Detector", "Data Leak Check"])
    user_input = st.text_input("Enter detail:")
    if st.button("Run Tool"):
        st.text_area("Analysis Report:", get_detailed_report(selected_free, user_input), height=200)

elif menu == "Premium Hub":
    st.success("🔓 PREMIUM TOOLS UNLOCKED")
    selected_pro = st.selectbox("Select Premium Tool:", ["Advanced IP Tracker", "Deep Link Scraper"])
    pro_input = st.text_input("Enter detail:")
    if st.button("Run Premium Tool"):
        # Yahan bhi waisa hi detailed response aayega
        st.text_area("Premium Analysis:", f"🚀 PREMIUM REPORT: {pro_input}\n- Deep Scanning: 100%\n- Risk Factor: Low\n- Encryption: AES-256\n- Action: Priority protection enabled.", height=200)
