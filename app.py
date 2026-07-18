# Yeh code aapke Premium section mein add karein
st.subheader("Upgrade to Premium (Manual Payment)")

# Apni UPI ID yahan daalein
my_upi_id = "aapki_upi_id@bankname" 
pay_link = f"upi://pay?pa={my_upi_id}&pn=CyberMind&cu=INR"

st.write("Premium access lene ke liye niche button dabayein aur payment complete karein:")

# Button jo seedha UPI app khol dega
st.link_button("Pay via UPI (GooglePay/PhonePe)", pay_link)

st.write("---")
st.write("Payment ke baad, is button par click karke mujhe screenshot bhejein:")
st.link_button("Confirm Payment on WhatsApp", "https://wa.me/91XXXXXXXXXX?text=Maine payment kar diya hai, please mujhe Premium activate karke dein.")
