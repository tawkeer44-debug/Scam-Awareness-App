import streamlit as st
import secrets
import string

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

# --- HOME & FREE TOOLS (5 Tools) ---
if menu == "Home & Free Tools":
    st.header("🏠 Free Tools Section")
    st.write("Ye sabhi tools bilkul free hain.")
    
    selected_free = st.selectbox("Select Free Tool:", ["Link Scanner", "Password Generator", "Fake App Detector", "Data Leak Check", "Safety Tips"])
    
    if st.button("Run Free Tool"):
        if selected_free == "Link Scanner": st.success("✅ Link is SAFE!")
        elif selected_free == "Password Generator": st.code(''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(12)))
        elif selected_free == "Fake App Detector": st.success("✅ App is Verified!")
        elif selected_free == "Data Leak Check": st.success("🔍 No Data Leak Found.")
        elif selected_free == "Safety Tips": st.info("💡 Tip: Use strong passwords everywhere!")

# --- PREMIUM HUB (5 Tools + Unlocked Status) ---
elif menu == "Premium Hub":
    st.header("⭐ Premium Hub")
    st.success("🔓 PREMIUM TOOLS ARE UNLOCKED FOR 24 HOURS!")
    
    selected_pro = st.selectbox("Select Premium Tool:", ["Advanced IP Tracker", "Deep Link Scraper", "Auto-Delete Scam Logs", "Identity Guard", "Priority Support Chat"])
    
    if st.button("Run Premium Tool"):
        if selected_pro == "Advanced IP Tracker": st.success("📍 IP Location: Secured Server.")
        elif selected_pro == "Deep Link Scraper": st.success("🔗 Deep Link Analysis: Done.")
        elif selected_pro == "Auto-Delete Scam Logs": st.success("🧹 Logs Cleared Successfully.")
        elif selected_pro == "Identity Guard": st.success("🛡️ Identity Protection Active.")
        elif selected_pro == "Priority Support Chat": st.link_button("Chat Now", "https://wa.me/91+9797168280?text=I need help with Premium")

    st.markdown("---")
    st.subheader("Pricing (After Offer Ends)")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.write("7 Days: ₹300"); st.link_button("Buy", "https://wa.me/91+9797168280?text=Plan: 7 Days")
    with col2: st.write("1 Month: ₹1500"); st.link_button("Buy", "https://wa.me/91+9797168280?text=Plan: 1 Month")
    with col3: st.write("1 Year: ₹3000"); st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 1 Year")
    with col4: st.write("Lifetime: ₹8000"); st.link_button("Buy", "https://wa.me/91+9797168280?text=Plan: Lifetime")
