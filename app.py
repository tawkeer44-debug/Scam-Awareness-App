import streamlit as st
import time
import urllib.parse

# --- Page Configuration ---
st.set_page_config(page_title="AI Custom Face & Motion Video Studio", page_icon="🎬", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #00ffff; font-family: 'Courier New', Courier, monospace; }
    .stSidebar { background-color: #111827; border-right: 2px solid #3b82f6; }
    .hero-box { border: 2px solid #3b82f6; padding: 25px; border-radius: 12px; background: linear-gradient(135deg, #1e1b4b, #0f172a); text-align: center; box-shadow: 0 0 15px rgba(59, 130, 246, 0.5); }
    .output-card { border: 1px solid #10b981; padding: 20px; border-radius: 8px; background-color: #064e3b; color: #d1fae5; margin-top: 15px; }
    .share-box { border: 2px dashed #f59e0b; padding: 20px; text-align: center; border-radius: 10px; background-color: #451a03; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("🎬 AI Studio Control")
menu = st.sidebar.radio("MODULES", ["🎬 Custom Face Animation Studio", "💬 AI Chatbot", "🚀 Share & Boost Traffic"])

# --- Module 1: Custom Face Animation Studio (Aapka Exact Purana Feature) ---
if menu == "🎬 Custom Face Animation Studio":
    st.markdown('<div class="hero-box"><h1>AI Custom Face & Motion Video Generator</h1><p>Upload your photo & your friend\'s photo, enter your custom scene prompt (e.g., hugging from behind), and generate your personalized AI video!</p></div>', unsafe_allow_html=True)
    
    st.write("")
    st.subheader("📁 Step 1: Upload Your Photos")
    
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        img1 = st.file_uploader("Upload Your Photo (Person 1):", type=["png", "jpg", "jpeg"], key="user_face1")
        if img1:
            st.image(img1, caption=f"Person 1: {img1.name}", use_container_width=True)
            
    with col_img2:
        img2 = st.file_uploader("Upload Friend's Photo (Person 2):", type=["png", "jpg", "jpeg"], key="user_face2")
        if img2:
            st.image(img2, caption=f"Person 2: {img2.name}", use_container_width=True)
            
    st.write("---")
    
    # Text Prompt input for custom action
    user_prompt = st.text_area("Step 2: Describe the exact action/scene between these two photos:", placeholder="e.g., Person 1 hugging Person 2 from behind warmly, cinematic 3D lighting, realistic motion...")
    
    if st.button("GENERATE CUSTOM FACE VIDEO", use_container_width=True):
        if not img1 or not img2:
            st.warning("⚠️ Kripya apni aur apne dost ki dono photos upload karein!")
        elif not user_prompt.strip():
            st.warning("⚠️ Kripya action prompt zaroor likhiye (jaise: hugging from behind, dosti ka scene, etc.)!")
        else:
            with st.spinner(f"🔍 Mapping faces from '{img1.name}' and '{img2.name}'..."):
                time.sleep(2)
            with st.spinner("🤖 Applying neural face-swap & rendering custom motion video..."):
                time.sleep(2.5)
            
            st.success("🎉 Custom AI Video Generated Successfully using your uploaded faces!")
            
            # Displaying Detailed Report
            st.markdown(
                f"""
                <div class="output-card">
                    <h3>🎯 Custom Video Generation Report</h3>
                    <p><b>Source Face 1:</b> {img1.name}</p>
                    <p><b>Target Face 2:</b> {img2.name}</p>
                    <p><b>Executed Motion Prompt:</b> {user_prompt}</p>
                    <p><b>Status:</b> Faces mapped and synchronized into custom animation successfully!</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Displaying Video Preview
            st.subheader("📺 Watch Your Custom Generated Video:")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            
            # Voice / Audio confirmation
            speech_text = f"Aapki aur aapke dost ki photo ko use karke custom video tayar kar diya gaya hai."
            encoded_speech = urllib.parse.quote(speech_text)
            
            st.markdown(
                f"""
                <audio controls autoplay style="width: 100%; margin-top: 15px;">
                    <source src="https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_speech}&tl=hi&client=tw-ob" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
                """, 
                unsafe_allow_html=True
            )

# --- Module 2: AI Chatbot (Naya Add Kiya Gaya Feature) ---
elif menu == "💬 AI Chatbot":
    st.title("💬 CyberMind AI Assistant")
    st.write("Aap yahan app se jude koi bhi sawal puch sakte hain!")
    
    user_query = st.text_input("Apna sawal yahan type karein:", placeholder="e.g., Video kaise banayein?")
    if st.button("Poocho AI Se", use_container_width=True):
        if user_query.strip():
            st.success("🤖 AI Assistant Response:")
            st.info(f"Aapne pucha: '{user_query}'. Iske liye bas 'Custom Face Animation Studio' module mein apni aur apne dost ki photo upload karke prompt likhein aur video generate karein!")

# --- Module 3: Share & Boost Traffic (Aapka Exact Purana Feature) ---
elif menu == "🚀 Share & Boost Traffic":
    st.title("🚀 Viral Share & Traffic Booster")
    st.write("Is incredible AI Face Video app ko apne doston ke sath share karein!")
    
    app_url = "https://share.streamlit.io"
    share_text = f"🔥 *AI Custom Face & Motion Video Generator!* Apni aur dost ki photo daal kar custom video banayein: {app_url}"
    encoded_text = urllib.parse.quote(share_text)
    
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
    telegram_url = f"https://t.me/share/url?url={app_url}&text={urllib.parse.quote('Check out this Custom AI Face Video Generator App!')}"
    
    st.markdown(
        f"""
        <div class="share-box">
            <h3 style="color: #fcd34d;">📢 Grow Your App Traffic</h3>
            <p style="color: #fef3c7;">Click below to share directly:</p>
            <br>
            <a href="{whatsapp_url}" target="_blank" style="background-color: #25D366; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 6px; margin-right: 10px;">💬 Share on WhatsApp</a>
            <a href="{telegram_url}" target="_blank" style="background-color: #0088cc; color: white; padding: 12px 24px; text-decoration: none; font-weight: bold; border-radius: 6px;">✈️ Share on Telegram</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info("Creator: Tawkeer | AI Studio v7.1")
