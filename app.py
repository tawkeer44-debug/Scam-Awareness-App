import streamlit as st
from openai import OpenAI

# Page Config
st.set_page_config(page_title="CyberMind AI Pro-Suite", layout="wide", page_icon="🛡️")

# --- SIDEBAR NAVIGATION (Professional Look) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=80)
    st.title("CyberMind AI")
    st.markdown("---")
    menu = st.sidebar.radio("Navigation", [
        "🛡️ Scam Analyzer", 
        "🎨 AI Image Generator", 
        "🔍 URL Validator", 
        "🔐 Password Strength", 
        "📝 Text Summarizer", 
        "🌐 IP Tracker", 
        "💻 Code Debugger", 
        "📊 Data Insights", 
        "🤖 AI Chatbot", 
        "🛠️ System Health"
    ])
    st.markdown("---")
    st.success("All Systems Operational")

# --- FEATURES ---
def scam_analyzer():
    st.header("🔍 Scam Analyzer")
    text = st.text_area("Paste message:")
    if st.button("Scan"):
        st.write("Checking for phishing patterns...")

def image_generator():
    st.header("🎨 AI Image Generator")
    prompt = st.text_input("Describe your image:")
    if st.button("Generate"):
        # Yahan apni API Key daalein
        api_key = "SK-YOUR-API-KEY-HERE" 
        try:
            client = OpenAI(api_key=api_key)
            response = client.images.generate(prompt=prompt, n=1, size="1024x1024")
            st.image(response.data[0].url)
        except:
            st.error("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")

# --- APP LOGIC ---
if menu == "🛡️ Scam Analyzer":
    scam_analyzer()
elif menu == "🎨 AI Image Generator":
    image_generator()
else:
    st.header(f"You selected: {menu}")
    st.info("This feature is currently being initialized by the CyberMind Engine.")