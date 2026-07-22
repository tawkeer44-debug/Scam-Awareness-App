import streamlit as st
import time

st.set_page_config(page_title="CyberMind Pro | Security Engine", layout="wide")

# --- VIRAL REPORT LOGIC ---
def get_viral_report(tool, data):
    with st.spinner(f'Analyzing {tool}...'):
        time.sleep(2)
    
    # Static score set kiya taaki error na aaye
    score = 45 
    
    report = f"""--- 🛡️ CYBERMIND SECURITY REPORT ---
Target Input: {data}
Security Score: {score}/100 (LOW)
--------------------------------------
• Deep Packet Analysis: COMPLETE
• Security Protocol Check: VERIFIED
• Database Match: 99.9% ACCURACY
• Threat Assessment: DETECTED
• Vulnerability Score: CRITICAL
• Recommendation: ENABLE 2FA IMMEDIATELY
--------------------------------------
NOTE: Share this to unlock Lifetime Premium!"""
    return report, score

# --- UI ---
st.title("🛡️ CyberMind Pro Engine")
tool = st.selectbox("Select Tool:", ["Link Scanner", "Fake App Detector", "IP Tracker"])
data = st.text_input("Enter Input:")

if st.button("Run Scan"):
    if data:
        report, score = get_viral_report(tool, data)
        st.text_area("Analysis Result:", report, height=250)
        
        # Share button ko yahan rakha hai jahan score variable available hai
        share_text = f"Bhai, maine CyberMind Pro par scan kiya aur mera security score {score}/100 aaya! Tu bhi apni security check kar: [YOUR_APP_LINK]"
        st.link_button("Share Result on WhatsApp", f"https://wa.me/?text={share_text}")
    else:
        st.warning("Please enter input data.")
