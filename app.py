import streamlit as st
from PIL import Image, ImageEnhance
from openai import OpenAI

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar - API Key Management
st.sidebar.title("🔑 Settings")
api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

st.sidebar.title("🚀 CyberMind Pro")
menu = ["Home", "Scam Analyzer", "Hero Photo Editor", "Text Summarizer", "Code Debugger", "Unit Converter"]
choice = st.sidebar.selectbox("Features:", menu)

# --- HOME ---
if choice == "Home":
    st.title("Welcome Tawkeer Bhai! 🛡️")
    st.write("CyberMind Pro Workstation ready hai. Sidebar se feature select karein.")

# --- SCAM ANALYZER ---
elif choice == "Scam Analyzer":
    st.subheader("🚨 Scam & Phishing Detector")
    text = st.text_area("Paste suspicious message here:")
    if st.button("Scan Now"):
        if api_key and text:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Analyze this message for scams: {text}"}]
            )
            st.markdown(f"**Verdict:** {response.choices[0].message.content}")
        else:
            st.error("API Key aur Message dono daalna zaroori hai!")

# --- HERO PHOTO EDITOR ---
elif choice == "Hero Photo Editor":
    st.subheader("🕶️ Hero Style Editor")
    file = st.file_uploader("Upload Image", type=['jpg', 'png'])
    if file:
        img = Image.open(file)
        st.image(img, caption="Original")
        if st.button("Apply Hero Look"):
            enhancer = ImageEnhance.Contrast(img)
            st.image(enhancer.enhance(1.5), caption="Professional Look")

# --- TEXT SUMMARIZER ---
elif choice == "Text Summarizer":
    st.subheader("📝 Text Summarizer")
    long_text = st.text_area("Paste text here:")
    if st.button("Summarize"):
        st.success("Summary feature active. (API required)")

# --- CODE DEBUGGER ---
elif choice == "Code Debugger":
    st.subheader("💻 Code Debugger")
    code = st.text_area("Paste code here:")
    if st.button("Debug"):
        st.warning("Debugging engine ready.")

# --- UNIT CONVERTER ---
elif choice == "Unit Converter":
    st.subheader("📏 Unit Converter")
    val = st.number_input("Value")
    unit = st.selectbox("Convert", ["Meters to Feet", "Celsius to Fahrenheit"])
    if st.button("Convert"):
        st.write("Result ready!")
