import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- AI SETUP (GROQ) ---
# Check karein ki aapne Secrets mein GROQ_API_KEY set kiya hai
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Error: Streamlit Secrets mein 'GROQ_API_KEY' set nahi hai.")

def get_groq_answer(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192", # Groq ka model
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {str(e)}"

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
    user_input = st.text_input("Enter Command / Question:", placeholder="Type your query here...")
    
    if st.button("SUBMIT COMMAND"):
        if "client" in globals() and user_input:
            with st.spinner("Analyzing..."):
                answer = get_groq_answer(user_input)
                st.markdown("### RESULT:")
                st.markdown(answer)
        elif "client" not in globals():
            st.error("Groq Client configure nahi hua hai.")
        else:
            st.warning("Please enter a command.")

elif menu == "PREMIUM HUB":
    st.write("---")
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
