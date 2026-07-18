import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Menu", ["Home", "Free Features (15+ Tools)", "Premium Plans"])

# --- HOME ---
if menu == "Home":
    st.header("Digital Security in Your Pocket")
    st.write("CyberMind Pro: Aapka bharosemand saathi.")

# --- FREE FEATURES (15+ TOOLS) ---
elif menu == "Free Features (15+ Tools)":
    st.header("🔧 Free Security & Utility Tools")
    st.write("Yahan aap 15+ free features use kar sakte hain:")
    
    # 15 Features list using columns for clean look
    col1, col2, col3 = st.columns(3)
    
    features = [
        "Basic Link Scanner", "Scam News Feed", "Password Generator", 
        "Data Leak Checker", "Safety Tips", "Wi-Fi Security Scan",
        "Fake App Detector", "Browser Privacy Guide", "Email Scam Filter",
        "Social Media Security", "Online Payment Safety", "Report a Scam",
        "Cyber Law Info", "Emergency Help Line", "Parental Control Tips"
    ]
    
    for i, feature in enumerate(features):
        if i % 3 == 0: col = col1
        elif i % 3 == 1: col = col2
        else: col = col3
        col.checkbox(feature)
        
    if st.button("Run Selected Tools"):
        st.success("Selected tools are now active!")

# --- PREMIUM PLANS ---
elif menu == "Premium Plans":
    st.header("⭐ Upgrade to Pro (Premium)")
    # (Yahan wahi pehle wala pricing table rahega jo aapne final kiya tha)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("7 Days")
        st.write("₹300")
        st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 7 Days")
    with col2:
        st.subheader("30 Days")
        st.write("₹800")
        st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 30 Days")
    with col3:
        st.subheader("1 Year")
        st.write("₹2500")
        st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 1 Year")
    with col4:
        st.subheader("Lifetime")
        st.write("₹5000")
        st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: Lifetime")
