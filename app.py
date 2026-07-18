import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
st.sidebar.title("Navigation")

# Sidebar Menu
menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

# --- HOME & FREE TOOLS SECTION ---
if menu == "Home & Free Tools":
    st.header("Welcome to CyberMind Pro")
    
    # Ye raha woh special offer jo aapne bataya
    st.warning("🔥 SPECIAL OFFER: Agle 24 ghante ke liye, pehle 50 users ko Premium features bilkul FREE milenge!")
    
    st.subheader("Select a Free Tool to get started:")
    
    free_tools = [
        "Select a tool...", "Basic Link Scanner", "Password Generator", 
        "Data Leak Checker", "Safety Tips", "Wi-Fi Security Scan",
        "Fake App Detector", "Browser Privacy Guide", "Email Scam Filter",
        "Social Media Security", "Online Payment Safety", "Report a Scam",
        "Cyber Law Info", "Emergency Help Line", "Parental Control Tips", "Anti-Phishing Guide"
    ]
    
    selected_tool = st.selectbox("Choose a tool from the list:", free_tools)
    
    if selected_tool != "Select a tool...":
        st.write(f"### You selected: {selected_tool}")
        if st.button(f"Run {selected_tool}"):
            st.success(f"{selected_tool} is now active!")

# --- PREMIUM HUB (Bilkul untouched) ---
elif menu == "Premium Hub":
    st.header("⭐ Premium Membership")
    st.write("Unlock advanced protection and priority support.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("7 Days")
        st.write("₹300")
        st.link_button("Buy 7 Days", "https://wa.me/9 6006777536?text=I want to buy 7 Days plan")
    with col2:
        st.subheader("30 Days")
        st.write("₹800")
        st.link_button("Buy 30 Days", "https://wa.me/91 6006777536?text=I want to buy 30 Days plan")
    with col3:
        st.subheader("1 Year")
        st.write("₹2500")
        st.link_button("Buy 1 Year", "https://wa.me/91 6006777536?text=I want to buy 1 Year plan")
    with col4:
        st.subheader("Lifetime")
        st.write("₹5000")
        st.link_button("Buy Lifetime", "https://wa.me/91 6006777536?text=I want to buy Lifetime plan")
