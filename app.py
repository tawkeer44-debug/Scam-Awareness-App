import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- AI SETUP (GROQ) ---
try:
    # Secrets se key uthao
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except Exception:
    st.error("Error: 'GROQ_API_KEY' set nahi hai! Streamlit Secrets mein jaakar check karein.")
    client = None

def get_groq_answer(prompt):
    if client:
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Groq API Error: {str(e)}"
    return "AI client configure nahi hua hai."

# --- SIDEBAR COMMANDS ---
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "FORENSICS", "CRYPTO MINER", "TRAFFIC MONITOR", 
    "PRO HACKER SUITE", "PREMIUM HUB"
])

# --- APP LOGIC ---
st.header(f"💀 {menu}")

if menu != "PREMIUM HUB":
    user_input = st.text_input("Enter Command:", placeholder="Enter your command here...")
    
    if st.button("SUBMIT COMMAND"):
        if user_input:
            with st.spinner("Analyzing..."):
                result = get_groq_answer(user_input)
                st.markdown("### RESULT:")
                st.write(result)
        else:
            st.warning("Pehle kuch likho toh!")

elif menu == "PREMIUM HUB":
    st.write("---")
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
