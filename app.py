import streamlit as st

# Custom CSS for modern look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .css-1v0mbdj { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# Page Configuration
st.set_page_config(page_title="CyberMind AI", page_icon="🛡️", layout="centered")

# Sidebar
st.sidebar.title("🛡️ CyberMind AI")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Report a Scam", "AI Image Generator", "AI Scam Checker"])

# Dashboard Section
if menu == "Dashboard":
    st.title("Welcome to CyberMind AI 🚀")
    st.info("Aapka apna smart digital security aur creative assistant.")
    st.warning("⚠️ Emergency Helpline: 1930")

# Report Section
elif menu == "Report a Scam":
    st.header("📢 Report a Scam")
    with st.form("report_form"):
        name = st.text_input("Aapka Naam")
        scam_type = st.selectbox("Scam Type", ["UPI", "Phishing", "Job Scam", "Other"])
        desc = st.text_area("Description")
        if st.form_submit_button("Submit Report"):
            st.success("Report successfully submitted to CyberMind AI!")

# AI Image Generator (New Feature)
elif menu == "AI Image Generator":
    st.header("🎨 AI Image Generator")
    st.write("Abhi ye feature test mode mein hai. Niche prompt likhein:")
    prompt = st.text_input("Describe the image you want...")
    if st.button("Generate Image"):
        if prompt:
            st.image("https://via.placeholder.com/400x200.png?text=AI+Generating+Image...", caption="Generating your imagination...")
            st.warning("Feature Connect: Gemini/Stable Diffusion API abhi set-up karna baaki hai.")
        else:
            st.error("Kripya kuch likhein!")

# AI Scam Checker
elif menu == "AI Scam Checker":
    st.header("🤖 AI Scam Checker")
    user_input = st.text_input("Link ya message paste karein:")
    if st.button("Verify Now"):
        st.write("CyberMind AI analysis in progress...")
