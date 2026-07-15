import streamlit as st
import google.generativeai as genai

# --- API CONFIGURATION ---
# Yeh line sabse zaruri hai, iske bina model kaam nahi karega
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("API Configuration Error: Check your Secrets settings.")

# --- RISK FUNCTION ---
def get_risk_score(text):
    try:
        response = model.generate_content(f"Analyze this for scam risk. Give a score from 0-100 and a short reason. Format: Score: [Number], Reason: [Text]. Input: {text}")
        return response.text
    except Exception as e:
        return "Error: Could not connect to AI. Please try again."

# --- APP UI ---
st.title("🛡️ CyberMind AI: Pro-Suite")
input_data = st.text_area("Analyze Link or Message:")

if st.button("RUN DEEP SCAN 🚀"):
    if input_data:
        with st.spinner("Executing Deep Forensic Scan..."):
            result = get_risk_score(input_data)
            st.success("SCAN COMPLETE")
            st.write(result)
    else:
        st.warning("Please enter some data to scan!")
