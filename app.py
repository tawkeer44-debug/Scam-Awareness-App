import streamlit as st
from PIL import Image
from rembg import remove
import io
from groq import Groq

# Page Config
st.set_page_config(page_title="CyberMind Pro", layout="wide")

# Sidebar Settings
st.sidebar.title("🚀 CyberMind Pro")
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

menu = ["Home", "Scam Analyzer", "URL Scanner", "Content Generator", "Explain Like I'm 5", "Translator", "Photo Editor", "Code Debugger"]
choice = st.sidebar.selectbox("Features:", menu)

def get_groq_client(api_key):
    return Groq(api_key=api_key)

# --- HOME ---
if choice == "Home":
    st.title("Welcome Tawkeer Bhai! 🛡️")
    st.write("CyberMind Pro Workstation ready hai.")

# --- SCAM ANALYZER ---
elif choice == "Scam Analyzer":
    st.subheader("🚨 Scam & Phishing Detector")
    text = st.text_area("Paste suspicious message:")
    if st.button("Scan Now"):
        if groq_api_key and text:
            client = get_groq_client(groq_api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Analyze this message for scams and phishing: {text}"}]
            )
            st.markdown(f"### Verdict:\n{response.choices[0].message.content}")

# --- URL SCANNER ---
elif choice == "URL Scanner":
    st.subheader("🌐 Smart URL Safety Checker")
    url = st.text_input("Paste URL here:")
    if st.button("Analyze Link"):
        client = get_groq_client(groq_api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Is this URL safe or malicious? {url}"}]
        )
        st.info(response.choices[0].message.content)

# --- CONTENT GENERATOR ---
elif choice == "Content Generator":
    st.subheader("📝 YouTube/Social Media Script Writer")
    topic = st.text_input("Topic for your video/post:")
    if st.button("Generate Script"):
        client = get_groq_client(groq_api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Write a professional script/post about: {topic}"}]
        )
        st.write(response.choices[0].message.content)

# --- EXPLAIN LIKE I'M 5 ---
elif choice == "Explain Like I'm 5":
    st.subheader("🧠 Simplified Tech Explainer")
    concept = st.text_input("Enter technical concept:")
    if st.button("Simplify"):
        client = get_groq_client(groq_api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Explain {concept} as if I am 5 years old."}]
        )
        st.success(response.choices[0].message.content)

# --- TRANSLATOR ---
elif choice == "Translator":
    st.subheader("🔠 Scam Message Translator")
    msg = st.text_area("Paste message in any language:")
    if st.button("Translate & Detect"):
        client = get_groq_client(groq_api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Translate this to English and detect scam risk: {msg}"}]
        )
        st.write(response.choices[0].message.content)

# --- PHOTO EDITOR ---
elif choice == "Photo Editor":
    st.subheader("🖼️ AI Background Remover")
    file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, caption="Original", use_container_width=True)
        if st.button("Remove Background"):
            with st.spinner("Processing..."):
                input_data = file.getvalue()
                output_data = remove(input_data)
                img_output = Image.open(io.BytesIO(output_data))
                st.image(img_output, caption="Background Removed", use_container_width=True)
                buf = io.BytesIO()
                img_output.save(buf, format="PNG")
                st.download_button("Download Edited Photo", buf.getvalue(), "edited_photo.png", "image/png")

# --- CODE DEBUGGER ---
elif choice == "Code Debugger":
    st.subheader("💻 Engineering Code Debugger")
    code = st.text_area("Paste broken code:")
    if st.button("Debug Code"):
        client = get_groq_client(groq_api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Fix and explain: {code}"}]
        )
        st.code(response.choices[0].message.content)