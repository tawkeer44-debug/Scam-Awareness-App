import streamlit as st
from groq import Groq
import os

# --- FIX: Key ko hard-code karke check karte hain ---
# Yahan apni ASLI KEY daal dein (gsk_...)
GROQ_API_KEY = "gsk_yahan_apni_asli_key_paste_karein" 

# Agar secrets mein hai, toh wahan se le lo, warna upar wali use karo
api_key = st.secrets.get("GROQ_API_KEY", GROQ_API_KEY)

client = Groq(api_key=api_key)
import streamlit as st
import google.generativeai as genai

# --- PRO SETTINGS ---
st.set_page_config(page_title="CyberMind Pro", layout="centered")

# --- RISK METER FUNCTION ---
def get_risk_score(text):
    # Pro Logic: AI se score mangwate hain
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"Analyze this for scam risk. Give a score from 0-100 and a short reason. Format: Score: [Number], Reason: [Text]. Input: {text}")
    return response.text

st.title("🛡️ CyberMind AI: Pro-Suite")

input_data = st.text_area("Analyze Link or Message:")

if st.button("RUN DEEP SCAN 🚀"):
    if input_data:
        with st.spinner("Executing Deep Forensic Scan..."):
            result = get_risk_score(input_data)
            
            # --- PRO UI ---
            st.success("SCAN COMPLETE")
            
            # Risk Meter logic
            st.subheader("📊 Risk Assessment")
            score = 75 # Yahan aap AI response se score nikal sakte hain
            st.progress(score)
            
            st.write(f"**Analysis:** {result}")
            
            # Pro Action Button
            if st.button("Download Security Report"):
                st.download_button("Download PDF", data=result, file_name="report.txt")
    else:
        st.error("Input missing!")