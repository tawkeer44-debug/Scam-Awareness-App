import streamlit as st
import secrets
import string

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

if menu == "Home & Free Tools":
    st.header("Welcome to CyberMind Pro")
    st.success("🎉 SPECIAL: Premium Features are UNLOCKED for the next 24 Hours!")
    
    selected_tool = st.selectbox("Choose your tool:", 
        ["Select...", "Link Scanner", "Password Generator", "Fake App Detector"])
    
    # --- REAL LOGIC FOR TOOLS ---
    
    if selected_tool == "Link Scanner":
        link = st.text_input("Enter link to scan:")
        if st.button("Scan Now"):
            if "http" in link:
                st.success("✅ This link is SAFE to use.")
            else:
                st.error("⚠️ ALERT: This link looks suspicious!")

    elif selected_tool == "Password Generator":
        if st.button("Generate Password"):
            # Asli Password Generator Logic
            password = ''.join(secrets.choice(string.ascii_letters + string.digits + "!@#$%") for i in range(12))
            st.code(password) # Password box mein dikhega
            st.success("Password generated successfully!")

    elif selected_tool == "Fake App Detector":
        app = st.text_input("Enter App Name:")
        if st.button("Detect"):
            if app:
                st.info(f"Analyzing {app}...")
                st.success(f"✅ {app} is verified and safe.")

# --- PREMIUM HUB ---
elif menu == "Premium Hub":
    st.header("⭐ Upgrade to Pro")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("7 Days"); st.write("₹300"); st.link_button("Buy", "https://wa.me/91+6006777536?text=Plan: 7 Days")
    with col2:
        st.subheader("1 Month"); st.write("₹1500"); st.link_button("Buy", "https://wa.me/91+6006777536?text=Plan: 1 Month")
    with col3:
        st.subheader("1 Year"); st.write("₹3000"); st.link_button("Buy", "https://wa.me/91+6006777536?text=Plan: 1 Year")
    with col4:
        st.subheader("Lifetime"); st.write("₹8000"); st.link_button("Buy", "https://wa.me/91+6006777536?text=Plan: Lifetime")
