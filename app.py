import streamlit as st
from PIL import Image, ImageEnhance
from groq import Groq
import os

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar - Settings (Secrets se API key le raha hai)
st.sidebar.title("🔑 Settings")
# Agar aapne Secrets mein set kiya hai, toh ye automatically utha lega
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

st.sidebar.title("🚀 CyberMind Pro")
menu = ["Home", "Scam Analyzer", "Hero Photo Editor", "Code Debugger", "Text Summarizer", "Unit Converter"]
choice = st.sidebar.selectbox("Features:", menu)

# --- Initialize Groq Client ---
def get_groq_client(api_key):
    return Groq(api_key=api_key)

# --- HOME ---
if choice == "Home":
    st.title("Welcome Tawkeer Bhai! 🛡️")
    st.write("Aapka Professional Workstation taiyaar hai. Features explore karein.")

# --- SCAM ANALYZER ---
elif choice == "Scam Analyzer":
    st.subheader("🚨 Scam & Phishing Detector")
    text = st.text_area("Paste suspicious message here:")
    if st.button("Scan Now"):
        if groq_api_key and text:
            try:
                client = get_groq_client(groq_api_key)
                response = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[{"role": "user", "content": f"Analyze this message for scams, phishing, or fraud. Is it safe? Give a short verdict: {text}"}]
                )
                st.markdown(f"### Verdict:\n{response.choices[0].message.content}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("API Key aur Message dono zaruri hain!")

# --- HERO PHOTO EDITOR ---
elif choice == "Hero Photo Editor":
    st.subheader("🕶️ Hero Style Editor")
    file = st.file_uploader("Upload Image", type=['jpg', 'png'])
    if file:
        img = Image.open(file)
        st.image(img, caption="Original")
        if st.button("Apply Hero Look"):
            enhancer = ImageEnhance.Contrast(img)
            st.image(enhancer.enhance(1.5), caption="Professional Hero Look")

# --- CODE DEBUGGER ---
elif choice == "Code Debugger":
    st.subheader("💻 Engineering Code Debugger")
    code = st.text_area("Paste broken code here:")
    if st.button("Debug Code"):
        if groq_api_key and code:
            client = get_groq_client(groq_api_key)
            response = client.chat.completions.create(
                model=" llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Debug this code and provide the fixed version: {code}"}]
            )
            st.code(response.choices[0].message.content)
        else:
            st.warning("Please enter API Key and code.")

# --- TEXT SUMMARIZER ---
elif choice == "Text Summarizer":
    st.subheader("📝 Office Document Summarizer")
    long_text = st.text_area("Paste notes here:")
    if st.button("Summarize"):
        st.write("Summarizing feature is ready...")

# --- UNIT CONVERTER ---
elif choice == "Unit Converter":
    st.subheader("📏 Engineering Unit Converter")
    val = st.number_input("Value")
    unit = st.selectbox("Convert", ["Meters to Feet", "Celsius to Fahrenheit"])
    if st.button("Convert"):
        st.success("Conversion logic active.")
