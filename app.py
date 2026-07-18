import streamlit as st
import random
import string
from groq import Groq

st.set_page_config(page_title="CyberMind Pro", layout="wide", page_icon="🛡️")

# --- FREE FEATURES (5) ---
# 1. Scam Analyzer | 2. URL Scanner | 3. Password Generator 
# 4. Emergency Directory | 5. Cyber Safety Tips

# --- PREMIUM FEATURES (5) ---
# 1. Deep File Scanner | 2. Real-Time Alert System 
# 3. Personal Cloud Notes | 4. Multilingual Peter | 5. Ad-Free Experience

# Sidebar Navigation
st.sidebar.title("🚀 CyberMind Pro")
choice = st.sidebar.selectbox("Menu:", ["Home", "Scam Analyzer", "URL Scanner", "Password Generator", "Emergency Directory", "Safety Tips", "---", "💎 Premium Upgrade"])

# --- FREE FEATURES LOGIC ---
if choice == "Home":
    st.title("🛡️ Welcome to CyberMind Pro")
    st.write("Aapka personal Cyber Safety companion.")

elif choice == "Scam Analyzer":
    st.subheader("💻 Scam Analyzer (Free)")
    # Logic...

elif choice == "URL Scanner":
    st.subheader("🌐 URL Scanner (Free)")
    # Logic...

elif choice == "Password Generator":
    st.subheader("🎲 Password Generator (Free)")
    # Logic...

elif choice == "Emergency Directory":
    st.subheader("📞 Emergency Directory (Free)")
    st.write("Cyber Crime Helpline: 1930")

elif choice == "Safety Tips":
    st.subheader("💡 Daily Safety Tips (Free)")
    st.write("1. Kabhi bhi OTP kisi ko na batayein.\n2. Unknown links par click na karein.")

# --- PREMIUM UPGRADE PAGE ---
elif choice == "💎 Premium Upgrade":
    st.title("💎 Unlock Premium Features")
    st.write("Apni security ko professional level par le jayein!")
    
    # Grid of Premium Features
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        ### 🔓 Premium Unlock Karein:
        1. 📁 **Deep File Scanner:** PDF/Docs scan karein.
        2. 🔔 **Real-Time Alerts:** Scam hone se pehle janein.
        3. 🔒 **Cloud Notes:** Data sync aur encryption.
        4. 🗣️ **Hindi AI Peter:** Apni bhasha mein chat karein.
        5. 🚫 **Ad-Free:** Bina kisi distraction ke use karein.
        """)
    
    with c2:
        st.subheader("Choose Your Plan:")
        st.link_button("Buy 7 Days (₹49)", "YOUR_LINK")
        st.link_button("Buy Monthly (₹199)", "YOUR_LINK")
        st.link_button("Buy Yearly (₹999)", "YOUR_LINK")
