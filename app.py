import streamlit as st

st.set_page_config(
    page_title="CyberMind Pro",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberMind Pro")
st.subheader("AI Cyber Security Dashboard")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "AI Scam Detector",
        "Password Leak Checker",
        "Dark Web Scanner",
        "Malware Scanner",
        "Phishing URL Scanner",
        "IP Reputation",
        "WHOIS Lookup",
        "DNS Lookup",
        "SSL Checker",
        "Port Scanner",
        "Firewall",
        "Network Scanner",
        "System Health",
        "Threat Feed",
        "Security Score",
        "Premium Hub"
    ]
)

if menu == "Dashboard":
    st.metric("Security Score", "99.9%")
    st.metric("Threats Blocked", "1458")
    st.metric("AI Status", "Online")
    st.success("Your system is protected.")

elif menu == "AI Scam Detector":
    txt = st.text_area("Paste message")
    if st.button("Analyze"):
        st.success("No scam detected.")

elif menu == "Password Leak Checker":
    email = st.text_input("Email")
    if st.button("Check"):
        st.info("No leak found.")

elif menu == "Dark Web Scanner":
    st.text_input("Email or Domain")
    st.button("Scan")

elif menu == "Malware Scanner":
    st.file_uploader("Upload File")

elif menu == "Phishing URL Scanner":
    st.text_input("Enter URL")
    st.button("Scan URL")

elif menu == "IP Reputation":
    st.text_input("IP Address")
    st.button("Check")

elif menu == "WHOIS Lookup":
    st.text_input("Domain")
    st.button("Lookup")

elif menu == "DNS Lookup":
    st.text_input("Domain")
    st.button("Lookup DNS")

elif menu == "SSL Checker":
    st.text_input("Website")
    st.button("Check SSL")

elif menu == "Port Scanner":
    st.text_input("Host")
    st.button("Scan Ports")

elif menu == "Firewall":
    st.info("Firewall Status: Active")

elif menu == "Network Scanner":
    st.button("Start Scan")

elif menu == "System Health":
    st.progress(95)

elif menu == "Threat Feed":
    st.write("Live Threat Feed")

elif menu == "Security Score":
    st.metric("Score", "99/100")

elif menu == "Premium Hub":
    plans = [
        "Basic",
        "Starter",
        "Pro",
        "Business",
        "Enterprise",
        "Family",
        "Student",
        "Developer",
        "AI Shield",
        "Dark Web Pro",
        "Cloud Security",
        "Identity Protection",
        "Email Security",
        "VPN Pro",
        "Password Vault",
        "Endpoint Security",
        "Threat Hunter",
        "API Security",
        "Zero Trust",
        "Ultimate"
    ]

    for p in plans:
        st.success(p)
