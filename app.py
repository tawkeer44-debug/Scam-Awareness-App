import streamlit as st
import google.generativeai as genai

# --- PAGE SETUP ---
st.set_page_config(page_title="CyberMind AI", page_icon="🛡️", layout="wide")

# --- CUSTOM DESIGN (Khatarnak Look) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(90deg, #ff4b2b, #ff416c); color: white; font-weight: bold; }
    .css-1r6slp0 { background-color: #1c1f26; border-radius: 15px; padding: 20px; }
    h1, h2 { color: #ff416c; }
    .footer { position: fixed; bottom: 10px; width: 100%; text-align: center; font-size: 12px; color: grey; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR MENU ---
st.sidebar.title("🛡️ CyberMind AI")
menu = st.sidebar.radio("Navigation", ["Dashboard", "AI Scam Detector", "Image Lab", "Safety Hub"])

# --- CONTENT LOGIC ---
if menu == "Dashboard":
    st.title("Welcome to CyberMind AI")
    st.subheader("Advanced Digital Security Powered by AI")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800", use_container_width=True)
    st.info("Your Guardian against digital fraud.")

elif menu == "AI Scam Detector":
    st.header("🤖 AI Scam Detector")
    user_input = st.text_area("Paste suspicious message or link:")
    if st.button("Analyze Threat"):
        if user_input:
            try:
                # API Call
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(f"Analyze this for scam: {user_input}")
                st.markdown(f"### 🛡️ Analysis Result:\n{response.text}")
            except:
                st.error("API Key configure karein (Secrets settings mein).")
        else:
            st.warning("Please enter data to analyze.")

elif menu == "Image Lab":
    st.header("🎨 AI Image Lab")
    st.write("Advanced image generation features coming soon...")
    # Future integration place
    st.info("Tawkeer Yusuf is working on this module.")

# --- FOOTER (SIGNATURE) ---
st.markdown("""
    <div class="footer">
    Developed by <b>Tawkeer Yusuf</b> | Secured by CyberMind AI Engine
    </div>
    """, unsafe_allow_html=True)
