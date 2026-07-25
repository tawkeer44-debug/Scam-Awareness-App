import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- AI SETUP ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except:
    pass # Secret set hone par chalega

def get_ai_answer(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except:
        return "System error: API Key check karein."

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR COMMANDS ---
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "FORENSICS", "CRYPTO MINER", "TRAFFIC MONITOR", 
    "PRO HACKER SUITE", "PREMIUM HUB"
])

# --- LOGIC ---
st.header(f"💀 {menu}")

if menu != "PREMIUM HUB":
    cmd = st.text_input("Enter Command:", placeholder="Enter your command here...")
    if st.button("SUBMIT COMMAND"):
        with st.spinner("Analyzing..."):
            st.markdown(get_ai_answer(cmd))

elif menu == "PREMIUM HUB":
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
