import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="CyberMind X Pro", page_icon="🛡️", layout="wide")

# Custom CSS for that "Hacker" Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    h1 { color: #00ff00; font-family: 'Courier New', monospace; }
    .report-card { border: 1px solid #333; padding: 20px; border-radius: 10px; background-color: #1c1c1c; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛡️ CyberMind Command")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Link Analyzer", "Report a Scam"])

# Dashboard Section
if menu == "Dashboard":
    st.title("💻 CyberMind X Pro - Active")
    st.info("System Status: OPERATIONAL | Threat Level: LOW")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Live Users", "17", "+2")
    col2.metric("Threats Blocked", "42", "+5")
    col3.metric("System Uptime", "99.9%")
    
    st.markdown("---")
    st.subheader("Latest Security Alerts")
    st.warning("⚠️ High volume of Phishing links detected in your region.")

# Link Analyzer Section
elif menu == "Link Analyzer":
    st.title("🔍 Threat Scanner")
    link = st.text_input("Paste URL to check:")
    if st.button("RUN SCAN"):
        with st.spinner('Accessing secure databases...'):
            time.sleep(3)
            st.success("Scan Complete!")
            st.write("Analysis: No immediate threat found in this domain.")

# Report a Scam Section
elif menu == "Report a Scam":
    st.title("🚨 Report a Scam")
    with st.container():
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        name = st.text_input("Your Name")
        scam_type = st.selectbox("Type of Scam", ["Financial", "Social Media", "Phishing", "Other"])
        desc = st.text_area("Describe the scam")
        if st.button("SUBMIT REPORT"):
            st.success("Report submitted securely. Thank you for protecting the community!")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Project developed in memory of a vision.")
st.sidebar.write("Owner: Admin")
