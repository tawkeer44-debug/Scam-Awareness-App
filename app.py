import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
st.sidebar.title("Menu")

# Menu Selection
menu = st.sidebar.radio("Navigate", ["Home", "Features", "Premium Hub"])

# --- HOME ---
if menu == "Home":
    st.header("Welcome to CyberMind Pro")
    st.write("Stay safe, stay secure.")

# --- FEATURES (FREE & PRO MIX) ---
elif menu == "Features":
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Free Features")
        st.write("• Basic Link Scanner")
        st.write("• Scam Alert Notifications")
        if st.button("Run Link Scanner"):
            st.info("Scanner is ready! Enter your link below.")
            link = st.text_input("Enter link")
            if link:
                st.success("Scanning complete: Link is safe.")

    with col2:
        st.subheader("⭐ Pro Features")
        st.write("• Advanced Identity Guard")
        st.write("• Fraud Prevention Tracker")
        st.write("• Priority Support")
        st.error("🔒 Upgrade to Premium to unlock these!")
        if st.button("Unlock Pro"):
            st.warning("Go to Premium Hub to get access.")

# --- PREMIUM HUB ---
elif menu == "Premium Hub":
    st.header("⭐ Upgrade to Premium")
    st.write("Get full access to all tools.")
    
    # UPI Integration
    upi_id = "your_upi_id@bankname" 
    st.link_button("Pay via UPI (Premium)", f"upi://pay?pa={upi_id}&pn=CyberMind&cu=INR")
    st.link_button("Chat with Developer", "https://wa.me/91XXXXXXXXXX?text=I want to upgrade to Pro!")
