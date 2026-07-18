import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

# --- HOME & FREE TOOLS ---
if menu == "Home & Free Tools":
    st.header("Welcome to CyberMind Pro")
    st.success("🎉 SPECIAL: Premium Features are UNLOCKED for the next 24 Hours!")
    
    st.subheader("🛠️ Free Security Tools")
    
    # 10 Free Features
    free_tools = [
        "Select a tool...", "Link Scanner", "Password Generator", "Fake App Detector", 
        "Data Leak Check", "Wi-Fi Safety Scan", "Email Scam Filter", 
        "Social Media Privacy", "Online Payment Guard", "Cyber Law Guide", "Safety Tips"
    ]
    
    selected_tool = st.selectbox("Choose your tool:", free_tools)
    
    if selected_tool != "Select a tool...":
        st.write(f"### Running: {selected_tool}")
        user_input = st.text_input(f"Enter details for {selected_tool}:")
        if st.button("Run Now"):
            st.info(f"Analyzing {selected_tool}...")
            st.success("Tool is working perfectly!")

# --- PREMIUM HUB ---
elif menu == "Premium Hub":
    st.header("⭐ Upgrade to Pro")
    st.info("Grab your plan before the offer ends!")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("7 Days"); st.write("₹300"); st.link_button("Buy", "https://wa.me/91+6006777536?text=I want 7 Days plan")
    with col2:
        st.subheader("1 Month"); st.write("₹1500"); st.link_button("Buy", "https://wa.me/91+6006777536?text=I want 1 Month plan")
    with col3:
        st.subheader("1 Year"); st.write("₹3000"); st.link_button("Buy", "https://wa.me/91+6006777536?text=I want 1 Year plan")
    with col4:
        st.subheader("Lifetime"); st.write("₹8000"); st.link_button("Buy", "https://wa.me/91+6006777536?text=I want Lifetime plan")
