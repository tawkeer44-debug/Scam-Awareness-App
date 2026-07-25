import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- AI SETUP (Aapki API Key yahan dalni hogi) ---
# Tawkeer bhai, yahan apni key dalen: genai.configure(api_key="YOUR_API_KEY_HERE")
genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-pro')

# --- HACKER STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ff41; font-family: 'Courier New', monospace; }
    .stButton>button { border: 1px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    </style>
""", unsafe_allow_html=True)

# --- AI ENGINE ---
def get_ai_answer(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Error: API Key set nahi hai ya connection issue hai."

# --- SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
menu = st.sidebar.selectbox("COMMANDS", [
    "SECURITY LAB", "NETWORK MAPPER", "PASSWORD CRACKER", 
    "PRO HACKER SUITE", "PREMIUM HUB"
])

# --- DYNAMIC TOOL FUNCTION ---
def run_ai_tool(title):
    st.header(f"🛡️ {title}")
    st.write("---")
    user_input = st.text_input("Enter your question or command:", placeholder="e.g., How many components in water?")
    
    if st.button("SUBMIT"):
        if user_input:
            with st.spinner("Thinking..."):
                answer = get_ai_answer(user_input)
                st.markdown(f"**ANSWER:**\n\n{answer}")
        else:
            st.warning("Pehle kuch likho toh!")

# --- APP LOGIC ---

if menu == "SECURITY LAB":
    run_ai_tool("SECURITY LAB (AI Assistant)")

elif menu == "NETWORK MAPPER":
    run_ai_tool("NETWORK MAPPER (AI Assistant)")

elif menu == "PASSWORD CRACKER":
    run_ai_tool("PASSWORD CRACKER (AI Assistant)")

# --- PRO HACKER SUITE ---
elif menu == "PRO HACKER SUITE":
    st.header("💀 PRO HACKER SUITE")
    st.write("AI powered advanced exploits.")
    user_input = st.text_input("Enter exploit command:")
    if st.button("EXECUTE"):
        answer = get_ai_answer(user_input)
        st.markdown(f"**RESULT:**\n\n{answer}")

# --- PREMIUM HUB ---
elif menu == "PREMIUM HUB":
    st.header("💎 PREMIUM HUB")
    st.write("Direct contact for premium plans.")
    st.link_button("Contact on Instagram", "https://ig.me/m/th3_tawkeer")
