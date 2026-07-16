import streamlit as st
from PIL import Image, ImageEnhance
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar - Settings
st.sidebar.title("🔑 Settings")
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

st.sidebar.title("🚀 CyberMind Pro")
menu = ["Home", "Scam Analyzer", "Hero Photo Editor", "Code Debugger"]
choice = st.sidebar.selectbox("Features:", menu)

# --- Initialize Groq Client ---
def get_groq_client(api_key):
    return Groq(api_key=api_key)

# --- HOME ---
if choice == "Home":
    st.title("Welcome Tawkeer Bhai! 🛡️")
    st.write("CyberMind Pro Workstation ready hai.")

# --- SCAM ANALYZER ---
elif choice == "Scam Analyzer":
    st.subheader("🚨 Scam & Phishing Detector")
    text = st.text_area("Paste suspicious message here:")
    if st.button("Scan Now"):
        if groq_api_key and text:
            try:
                client = get_groq_client(groq_api_key)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", # Yahan naya model hai
                    messages=[{"role": "user", "content": f"Analyze this message for scams: {text}"}]
                )
                st.markdown(f"### Verdict:\n{response.choices[0].message.content}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("API Key aur Message daalna zaruri hai!")

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

# --- CODE DEBUGGER ---
elif choice == "Code Debugger":
    st.subheader("💻 Code Debugger")
    code = st.text_area("Paste code here:")
    if st.button("Debug"):
        if groq_api_key and code:
            client = get_groq_client(groq_api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile", # Yahan bhi naya model hai
                messages=[{"role": "user", "content": f"Fix this code: {code}"}]
            )
            st.code(response.choices[0].message.content)
        else:
            st.warning("API Key aur Code zaruri hai!")
