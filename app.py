import streamlit as st
from groq import Groq

# Yahan seedha apni key daal dein (Sirf test ke liye)
# Jab aapka kaam ban jaye, toh isse kisi ko share mat karna!
GROQ_API_KEY = "gsk_yahan_apni_asli_key_paste_karein" 

client = Groq(api_key=GROQ_API_KEY)

st.title("🛡️ CyberMind AI: Pro-Suite")
input_data = st.text_area("Analyze Link or Message:")

if st.button("RUN SCAN ⚡"):
    if input_data:
        with st.spinner("Analyzing..."):
            chat_completion = client.chat.completions.create(
                messages=[{"role": "system", "content": "Analyze for scam. Score 0-100 and reason."},
                          {"role": "user", "content": input_data}],
                model="llama3-8b-8192",
            )
            st.write(chat_completion.choices[0].message.content)
