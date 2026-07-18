import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

# --- HOME & FREE TOOLS ---
if menu == "Home & Free Tools":
    st.header("Welcome to CyberMind Pro")
    # Kal tak ke liye special offer
    st.error("🚀 PROMO: Premium Features are UNLOCKED for the next 24 Hours!")
    
    st.subheader("Free Tools")
    selected_tool = st.selectbox("Select Tool:", ["Select...", "Link Scanner", "Password Gen", "Security Tips"])
    
    if selected_tool == "Link Scanner":
        link = st.text_input("Paste link to scan:")
        if st.button("Scan"):
            st.success("Link is safe!")
    elif selected_tool == "Password Gen":
        if st.button("Generate"):
            st.success("Your secure password: Cyber#2026")

# --- PREMIUM HUB (Updated Pricing) ---
elif menu == "Premium Hub":
    st.header("⭐ Upgrade to Pro")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("7 Days")
        st.write("Price: ₹300")
        st.link_button("Buy", "https://wa.me/91+6006777536?text=I want 7 Days plan")
        
    with col2:
        st.subheader("1 Month")
        st.write("Price: ₹1500")
        st.link_button("Buy", "https://wa.me/91+6006777536?text=I want 1 Month plan")
        
    with col3:
        st.subheader("1 Year")
        st.write("Price: ₹3000")
        st.link_button("Buy", "https://wa.me/91+6006777536?text=I want 1 Year plan")
        
    with col4:
        st.subheader("Lifetime")
        st.write("Price: ₹8000")
        st.link_button("Buy", "https://wa.me/91+6006777536?text=I want Lifetime plan")
