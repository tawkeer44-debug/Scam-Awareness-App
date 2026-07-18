import streamlit as st

# Page configuration
st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro - Your Digital Safety App")
st.sidebar.title("Menu")

# Sidebar navigation
menu = st.sidebar.radio("Navigate", ["Home", "Scam Checker (Free)", "Premium Hub"])

# --- HOME SECTION ---
if menu == "Home":
    st.header("Welcome to CyberMind Pro")
    st.write("Hamara mission aapko online scams se bachana hai.")
    st.info("Free features ka use karein aur safe rahein!")

# --- FREE FEATURE: SCAM CHECKER ---
elif menu == "Scam Checker (Free)":
    st.header("🔍 Scam Link Analyzer")
    link = st.text_input("Enter the link to check:")
    
    if st.button("Analyze Link"):
        if link:
            # Yahan aap apna logic (if/else) laga sakte hain
            if "http" in link:
                st.success("This link seems okay, but stay cautious!")
            else:
                st.error("Invalid link format! Please enter a valid URL.")
        else:
            st.warning("Please enter a link first.")

# --- PREMIUM HUB ---
elif menu == "Premium Hub":
    st.header("⭐ Upgrade to Premium")
    st.write("Get advanced protection, personal advice, and direct support.")
    
    # UPI Section
    my_upi_id = "your_upi_id@bankname" # <--- Yahan apni UPI ID dalein
    pay_link = f"upi://pay?pa={my_upi_id}&pn=CyberMind&cu=INR"
    
    st.link_button("Pay via UPI (Premium)", pay_link)
    
    st.write("---")
    st.write("Payment ke baad screenshot bhejein:")
    st.link_button("Chat with Developer", "https://wa.me/91XXXXXXXXXX?text=I want to buy Premium!")
