import streamlit as st

# PWA (App Installable) settings ke liye metadata
st.set_page_config(page_title="Scam Awareness Portal", page_icon="🛡️")

# PWA ko enable karne ke liye ek chhota sa script (JS code)
st.markdown("""
<link rel="manifest" href="manifest.json">
<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js');
  }
</script>
""", unsafe_allow_html=True)

# Title aur Header
st.title("🛡️ Scam Awareness Portal")
st.subheader("Stay Alert, Stay Safe!")

# Urgent Help Section
st.warning("⚠️ Agar aapke saath fraud hua hai, toh turant 1930 par call karein (Cyber Crime Helpline) ya cybercrime.gov.in par report karein.")

# Tips Section
st.markdown("""
### ⚠️ Common Online Scams:
- **UPI Fraud:** Paise lene ke liye kabhi PIN mat daalein.
- **Fake Links:** Anjaan links par click na karein.
- **OTP Sharing:** OTP kabhi kisi ko na batayein.
- **Job Scams:** Pehle paise maangne walon se bachein.
""")

st.divider()

# Report Form
st.header("📢 Report a Scam")
with st.form("report_form"):
    name = st.text_input("Aapka Naam")
    phone = st.text_input("Aapka Mobile Number (Optional)")
    scam_type = st.selectbox("Scam ka prakar", ["UPI Fraud", "Phishing/Link", "Job Scam", "Other"])
    description = st.text_area("Scam ke baare mein thoda batayein (Date aur time bhi likhein)")
    
    submitted = st.form_submit_button("Report Submit Karein")

    if submitted:
        if name and description:
            st.success(f"Shukriya {name}! Humne aapki report note kar li hai.")
        else:
            st.error("Kripya Naam aur Description zaroor bharein.")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ | Dedicated to a safer digital future")
