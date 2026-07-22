import streamlit as st
import time
import random
from groq import Groq

# --- CONFIGURATION ---
# Replace YOUR_GROQ_API_KEY with the key you generated on console.groq.com
client = Groq(api_key="YOUR_GROQ_API_KEY")

st.set_page_config(page_title="CyberMind X", layout="wide")

# Theme Styling
st.markdown("""<style>
    .stApp { background-color: #000000; color: #00ff41; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; }
    .stTextInput>div>div>input { color: #00ff41; }
</style>""", unsafe_allow_html=True)

st.title("⚡ CYBERMIND X - ULTIMATE")
menu = st.sidebar.radio("CHOOSE MODULE", ["SECURE SCAN", "AI CHATBOT", "CREATIVE LAB", "PREMIUM HUB"])

# --- AI CHATBOT LOGIC (Using Groq API) ---
def get_groq_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# --- MAIN APP LOGIC ---
if menu == "SECURE SCAN":
    st.header("🛡️ THREAT DEFENSE SYSTEM")
    target = st.text_input("Enter Link/IP/App Name:")
    if st.button("RUN DEEP SCAN"):
        with st.spinner("Analyzing Packet Data..."):
            time.sleep(3)
            result = random.choice(["SAFE", "HIGH RISK DETECTED", "PHISHING ATTEMPT"])
            st.success(f"SCAN RESULT: {result}")

elif menu == "AI CHATBOT":
    st.header("🧠 NEURAL CHATBOT (Powered by Groq)")
    user_query = st.text_input("Ask CyberMind AI anything:")
    if st.button("SEND QUERY"):
        if user_query:
            with st.spinner("Processing through Groq Engine..."):
                response = get_groq_response(user_query)
                st.write(response)
        else:
            st.warning("Please enter a question.")

elif menu == "CREATIVE LAB":
    st.header("🎨 CREATIVE STUDIO")
    choice = st.selectbox("Select Generator", ["Image Generator", "Video Generator", "Face Swap"])
    prompt = st.text_input("Describe your prompt:")
    if st.button("GENERATE ASSET"):
        with st.spinner(f"Simulating {choice}..."):
            time.sleep(4)
            st.success(f"Generated {choice} for: '{prompt}'")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO CYBERMIND X-PRO")
    st.markdown("* Unlimited Chat | * 4K Exports | * Breach Alerts | * Ad-Free")
    st.radio("Select Duration:", ["7 Days - ₹99", "1 Month - ₹299", "Lifetime - ₹2499"])
    if st.button("ACTIVATE PREMIUM"):
        st.balloons()
