import streamlit as st
from PIL import Image, ImageEnhance
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar Settings
st.sidebar.title("🔑 Settings")
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

st.sidebar.title("🚀 CyberMind Pro")
menu = ["Home", "Scam Analyzer", "Hero Photo Editor", "Code Debugger"]
choice = st.sidebar.selectbox("Features:", menu)

def get_groq_client(api_key):
    return Groq(api_key=api_key)

# --- HOME ---
if choice == "Home":
    st.title("Welcome Tawkeer Bhai! 🛡️")
    st.write("CyberMind Pro Workstation active hai.")
    st.info("Features: Scam Detection, Code Debugging, aur Hero Photo Studio.")

# --- SCAM ANALYZER ---
elif choice == "Scam Analyzer":
    st.subheader("🚨 Scam & Phishing Detector")
    text = st.text_area("Paste suspicious message:")
    if st.button("Scan Now"):
        if groq_api_key and text:
            client = get_groq_client(groq_api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Analyze for scams: {text}"}]
            )
            st.markdown(f"### Verdict:\n{response.choices[0].message.content}")
        else:
            st.warning("Key aur Message dono dalen!")

# --- HERO PHOTO EDITOR ---
elif choice == "Hero Photo Editor":
    st.subheader("🕶️ Hero Style Studio")
    file = st.file_uploader("Upload Profile Image", type=['jpg', 'png'])
    if file:
        img = Image.open(file)
        st.image(img, caption="Original", use_container_width=True)
        style = st.selectbox("Choose Transformation:", 
                             ["Professional Look", "Leather Jacket Style", "Add Hero Beard", "Zero Fade Hairstyle"])
        if st.button("Apply Style"):
            enhancer = ImageEnhance.Contrast(img)
            st.image(enhancer.enhance(1.5), caption=f"Applied: {style}")
            st.warning("Note: Ye abhi basic filter hai. Advanced AI Generation ke liye hum 'Stability AI' API link karenge.")

# --- CODE DEBUGGER ---
elif choice == "Code Debugger":
    st.subheader("💻 Engineering Code Debugger")
    code = st.text_area("Paste broken code here:")
    if st.button("Debug Code"):
        if groq_api_key and code:
            client = get_groq_client(groq_api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Fix this code and explain changes: {code}"}]
            )
            st.code(response.choices[0].message.content)
        else:
            st.warning("Key aur Code dono dalen!")
