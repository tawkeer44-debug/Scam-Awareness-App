import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")

# --- NAVIGATION ---
menu = st.sidebar.radio("Menu", ["Home", "Free Features", "Premium Plans"])

if menu == "Home":
    st.header("Digital Security in Your Pocket")
    st.write("Welcome to CyberMind Pro. Keep yourself safe from online fraud.")

elif menu == "Free Features":
    st.header("Free Tools")
    st.write("Ye features aap abhi use kar sakte hain:")
    st.checkbox("Basic Link Scanner")
    st.checkbox("Fraud News Updates")
    st.checkbox("Safety Tips")
    if st.button("Use Scanner"):
        st.info("Scanner is active...")

elif menu == "Premium Plans":
    st.header("⭐ Upgrade to Pro (Premium)")
    st.write("Unlock advanced protection & features.")

    # Features list for Pro
    st.subheader("Pro Features Included:")
    st.write("✅ Identity Guard | ✅ Fraud Prevention Tracker | ✅ Priority Support | ✅ Real-time Alerts | ✅ Deep Analysis")

    # Pricing Plans
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("7 Days")
        st.write("₹300")
        st.link_button("Buy 7 Days", "https://wa.me/91XXXXXXXXXX?text=I want to buy 7 Days plan")

    with col2:
        st.subheader("30 Days")
        st.write("₹800")
        st.link_button("Buy 30 Days", "https://wa.me/91XXXXXXXXXX?text=I want to buy 30 Days plan")

    with col3:
        st.subheader("1 Year")
        st.write("₹2500")
        st.link_button("Buy 1 Year", "https://wa.me/91XXXXXXXXXX?text=I want to buy 1 Year plan")

    with col4:
        st.subheader("Lifetime")
        st.write("₹5000")
        st.link_button("Buy Lifetime", "https://wa.me/91XXXXXXXXXX?text=I want to buy Lifetime plan")

    st.warning("Note: Payment karne ke baad screenshot bhejein!")
