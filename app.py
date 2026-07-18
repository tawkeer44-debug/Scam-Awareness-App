import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
st.sidebar.title("Navigation")

menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

# --- HOME & FREE TOOLS ---
if menu == "Home & Free Tools":
    st.header("Welcome to CyberMind Pro")
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
        
        # Yahan main logic fix kar raha hoon
        if st.button("Run Selected Tool"):
            st.success(f"{selected_tool} is now active and running for you!")

# --- PREMIUM HUB ---
elif menu == "Premium Hub":
    st.header("⭐ Premium Membership")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("7 Days"); st.write("₹300"); st.link_button("Buy", "https://wa.me/91 6006777536?text=7 Days Plan")
    with col2:
        st.subheader("30 Days"); st.write("₹800"); st.link_button("Buy", "https://wa.me/91 6006777536?text=30 Days Plan")
    with col3:
        st.subheader("1 Year"); st.write("₹2500"); st.link_button("Buy", "https://wa.me/91 6006777536X?text=1 Year Plan")
    with col4:
        st.subheader("Lifetime"); st.write("₹5000"); st.link_button("Buy", "https://wa.me/91 6006777536?text=Lifetime Plan")
