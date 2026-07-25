import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- AI SETUP ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("API Key not found in Streamlit Secrets. Please add GOOGLE_API_KEY.")

def get_ai_answer(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# --- HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "FORENSICS", "CRYPTO MINER", "TRAFFIC MONITOR", 
    "PRO HACKER SUITE", "PREMIUM HUB"
])

# --- LOGIC ---
st.header(f"💀 {menu}")

if menu != "PREMIUM HUB":
    # User command input
    user_input = st.text_input("Enter Command / Question:", placeholder="Type your query here...")
    
    if st.button("SUBMIT COMMAND"):
        if user_input:
            with st.spinner("Processing..."):
                answer = get_ai_answer(user_input)
                st.markdown("### RESULT:")
                st.markdown(answer)
        else:
            st.warning("Please enter a command.")

elif menu == "PREMIUM HUB":
    st.write("---")
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    st.write(f"--- You selected: **{plan}** ---")
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
