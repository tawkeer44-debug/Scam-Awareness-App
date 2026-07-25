import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")

# --- HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; border-radius: 0px; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; border-radius: 0px; }
    .stSidebar { background-color: #050505; border-right: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- AI SETUP (GROQ) ---
try:
    # Key secrets se le rahe hain
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except Exception:
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
            return f"Groq Error: {str(e)}"
    return "API Key configure nahi hai. Secrets check karein."

# --- SIDEBAR COMMANDS ---
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "FORENSICS", "CRYPTO MINER", "TRAFFIC MONITOR", 
    "PRO HACKER SUITE", "PREMIUM HUB"
])

# --- APP LOGIC ---
st.title(f"💀 CYBERMIND X PRO")
st.subheader(f"COMMAND: {menu}")

if menu != "PREMIUM HUB":
    user_input = st.text_input("Enter Command / Query:", placeholder="Type here...")
    
    if st.button("EXECUTE"):
        if client is None:
            st.error("API Key missing! Secrets mein 'GROQ_API_KEY' set karein.")
        elif user_input:
            with st.spinner("Executing..."):
                result = get_groq_answer(user_input)
                st.markdown("---")
                st.markdown(result)
        else:
            st.warning("Command field empty hai.")

elif menu == "PREMIUM HUB":
    st.write("---")
    st.write("### Upgrade to Premium")
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
