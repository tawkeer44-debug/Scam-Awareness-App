import streamlit as st
import google.generativeai as genai

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

# --- AI SETUP (Safe - using Secrets) ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception:
    st.error("API Key set nahi hai! Streamlit Secrets mein 'GOOGLE_API_KEY' add karo.")

def get_ai_answer(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# --- SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
menu = st.sidebar.selectbox("COMMANDS", ["SECURITY LAB", "PRO HACKER SUITE", "PREMIUM HUB"])

# --- AI TOOL ENGINE ---
def run_ai_tool(title):
    st.header(f"🛡️ {title}")
    st.write("---")
    user_input = st.text_input("Enter your command or question:", placeholder="e.g., How many components in water?")
    
    if st.button("SUBMIT"):
        if user_input:
            with st.spinner("Analyzing..."):
                answer = get_ai_answer(user_input)
                st.markdown(f"**ANSWER:**\n\n{answer}")
        else:
            st.warning("Pehle kuch likho toh!")

# --- APP LOGIC ---

if menu == "SECURITY LAB":
    run_ai_tool("SECURITY LAB")

elif menu == "PRO HACKER SUITE":
    st.header("💀 PRO HACKER SUITE")
    if 'is_pro' not in st.session_state: st.session_state.is_pro = False
    
    if not st.session_state.is_pro:
        st.warning("⚠️ PRO FEATURES LOCKED.")
        if st.button("UNLOCK PRO ACCESS"):
            st.session_state.is_pro = True
            st.rerun()
    else:
        user_input = st.text_input("Enter pro command:", placeholder="e.g., Explain kernel security...")
        if st.button("EXECUTE"):
            answer = get_ai_answer(user_input)
            st.markdown(f"**RESULT:**\n\n{answer}")

elif menu == "PREMIUM HUB":
    st.header("💎 PREMIUM HUB")
    st.write("Select your plan to unlock full potential:")
    
    plan = st.radio("Available Plans:", ["7 Days", "1 Month", "6 Months", "1 Year", "Lifetime"])
    
    st.write(f"--- You selected: **{plan}** ---")
    st.write("To proceed with payment and activation, please contact me directly on Instagram.")
    
    # Instagram DM Link
    st.link_button(f"Message me for {plan} Plan", "https://ig.me/m/th3_tawkeer")
