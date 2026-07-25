import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide", page_icon="💀")

# --- HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- AI SETUP ---
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    client = None

def get_groq_answer(prompt, module_name):
    # Har module ka apna role/system prompt
    system_prompt = f"""You are a specialized AI assistant for {module_name}. 
    Only answer questions related to {module_name}. 
    If the user asks something outside the scope of {module_name}, 
    politely tell them: 'Yeh command {module_name} ke liye nahi hai, please sahi module mein query dalein.'"""

    if client:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    return "API Configuration missing."

# --- SIDEBAR ---
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "FORENSICS", "CRYPTO MINER", "TRAFFIC MONITOR", 
    "PRO HACKER SUITE"
])

# --- APP LOGIC ---
st.title(f"💀 CYBERMIND X PRO")
st.subheader(f"MODULE: {menu}")

if menu != "PREMIUM HUB":
    # Yahan module ke naam ke saath input change ho raha hai
    user_input = st.text_input(f"Enter {menu} Command:", placeholder=f"Type your {menu} query...")
    
    if st.button("EXECUTE"):
        if user_input:
            with st.spinner("Processing..."):
                result = get_groq_answer(user_input, menu)
                st.markdown("---")
                st.markdown(result)
        else:
            st.warning("Input box khali hai.")

# PREMIUM HUB ko alag rakha hai
if st.sidebar.button("PREMIUM HUB"):
    st.write("---")
    st.write("### Upgrade to Premium")
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
