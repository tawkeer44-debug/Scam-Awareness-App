import streamlit as st

# Page setup
st.set_page_config(page_title="CyberMind AI", page_icon="🛡️", layout="wide")

# Sidebar navigation
st.sidebar.title("🛡️ Portal Menu")
menu = st.sidebar.radio("Navigation", ["Home", "Report a Scam", "Safety Resources", "AI Scam Checker"])

# Home Section
if menu == "Home":
    st.title("🛡️ Welcome to Scam Awareness Portal")
    st.write("Hamara maqsad aapko digital fraud se bachana hai.")
    st.warning("⚠️ Agar fraud hua hai, toh 1930 par call karein ya cybercrime.gov.in par report karein.")

# Report Section
elif menu == "Report a Scam":
    st.header("📢 Report a Scam")
    with st.form("report_form"):
        name = st.text_input("Aapka Naam")
        scam_type = st.selectbox("Scam ka prakar", ["UPI Fraud", "Phishing", "Job Scam", "Other"])
        description = st.text_area("Details (Date/Time)")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success(f"Shukriya {name}! Report darj ho gayi hai.")

# Resources Section
elif menu == "Safety Resources":
    st.header("📖 Learn How to Stay Safe")
    st.markdown("""
    * **UPI:** PIN sirf paise katne ke liye hota hai, bhejne ke liye nahi.
    * **Links:** Anjaan links par kabhi click na karein.
    * **Jobs:** Pehle paise maangne wale hamesha fraud hote hain.
    """)

# AI Feature Placeholder
elif menu == "AI Scam Checker":
    st.header("🤖 AI Scam Checker")
    user_input = st.text_area("Message ya Link paste karein check karne ke liye:")
    if st.button("Check Now"):
        st.info("Feature under development! AI integration jaldi aayega.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Developed with ❤️")
