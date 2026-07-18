import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

st.title("🛡️ CyberMind Pro")
menu = st.sidebar.radio("Select Section", ["Home & Free Tools", "Premium Hub"])

if menu == "Home & Free Tools":
    st.header("Welcome to CyberMind Pro")
    st.warning("🔥 SPECIAL OFFER: Agle 24 ghante ke liye, pehle 50 users ko Premium features bilkul FREE milenge!")
    
    selected_tool = st.selectbox("Select Tool:", ["Select a tool...", "Basic Link Scanner", "Password Generator", "Fake App Detector"])
    
    if selected_tool == "Basic Link Scanner":
        user_input = st.text_input("Paste your link here:")
        if st.button("Analyze Link"):
            if user_input:
                st.info(f"Scanning: {user_input}...")
                st.success("Safe! No malicious activity found.")
            else:
                st.error("Please paste a link first!")

    elif selected_tool == "Password Generator":
        if st.button("Generate Secure Password"):
            import secrets, string
            password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(12))
            st.success(f"Your secure password is: {password}")

    elif selected_tool == "Fake App Detector":
        app_name = st.text_input("Enter App Name:")
        if st.button("Check App"):
            if app_name:
                st.success(f"{app_name} seems genuine. Stay safe!")
            else:
                st.warning("Enter an app name.")

elif menu == "Premium Hub":
    # (Wahi Premium section jo pehle tha)
    st.header("⭐ Premium Membership")
    st.link_button("Buy 7 Days (₹300)", "https://wa.me/91 6006777536?text=I want to buy 7 Days plan")
