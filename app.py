import streamlit as st
from groq import Groq

# 1. API Key Setup
# Agar secrets mein hai to wahan se, warna apni key yahan paste karein
api_key = st.secrets.get("GROQ_API_KEY", "gsk_yahan_apni_asli_key_paste_karein")
client = Groq(api_key=api_key)

st.title("🛡️ CyberMind AI: Pro-Suite")
input_data = st.text_area("Analyze Link or Message:")

# 2. Scan Logic
if st.button("RUN SCAN ⚡"):
    if input_data:
        with st.spinner("Executing Deep Forensic Scan..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a cyber security expert. Analyze the message for scams, phishing, or fraud. Provide a score from 0-100 and a clear explanation."},
                        {"role": "user", "content": input_data}
                    ],
                model="llama-3.1-8b-instant",
                )
                st.success("Scan Complete!")
                st.write(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste something to scan!")
