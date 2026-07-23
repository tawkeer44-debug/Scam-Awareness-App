# --- VIRAL SHARE FEATURE ---
def share_button():
    st.divider()
    st.subheader("🚀 VIRAL BOOST")
    st.write("Share this CyberMind X tool with your friends!")
    
    # Ye user ko status copy karne ka shortcut dega
    share_text = "I just scanned my phone with CyberMind X! 🛡️ Hackers can't touch me now. Check it out: [YOUR_APP_URL_HERE]"
    
    st.text_area("Share this status on WhatsApp/Instagram:", value=share_text)
    st.info("Copy the text above and post it on your Status!")
