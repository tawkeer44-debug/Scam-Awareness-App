import streamlit as st

st.set_page_config(page_title="Scam Awareness Portal", page_icon="🛡️")

st.title("🛡️ Scam Awareness Portal")
st.subheader("Stay Alert, Stay Safe!")

# Awareness Tips Section
st.markdown("""
### ⚠️ Common Online Scams to Watch Out For:
- **UPI Fraud:** Kabhi bhi paise receive karne ke liye PIN enter na karein.
- **Fake Links:** Kisi bhi anjaan link par click na karein, khas kar "KYC Update" wale messages.
- **OTP Sharing:** Bank se OTP kabhi kisi ko share na karein.
- **Job Scams:** "Work from home" ke naam par pehle paise maangne walon se savdhan rahein.
""")

st.divider()

# Report a Scam Section
st.header("📢 Report a Scam")
st.write("Kya aapke saath ya aapke kisi jaanne wale ke saath scam hua hai? Yahan report karein:")

with st.form("report_form"):
    name = st.text_input("Aapka Naam")
    scam_type = st.selectbox("Scam ka prakar", ["UPI Fraud", "Phishing/Link", "Job Scam", "Other"])
    description = st.text_area("Scam ke baare mein thoda batayein")
    submitted = st.form_submit_button("Report Submit Karein")

    if submitted:
        st.success(f"Shukriya {name}! Humne aapki report note kar li hai.")

st.info("Hum saath mil kar scams ke khilaf ladenge!")
