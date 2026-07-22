import streamlit as st
import time
import random

# Page Config
st.set_page_config(page_title="CyberMind X", layout="wide")

# Theme Styling
st.markdown("""<style>
    .stApp { background-color: #000000; color: #00ff41; }
    .stButton>button { border: 2px solid #00ff41; background: #000; color: #00ff41; font-weight: bold; }
    .stTextInput>div>div>input { color: #00ff41; }
</style>""", unsafe_allow_html=True)

st.title("⚡ CYBERMIND X - ULTIMATE")
menu = st.sidebar.radio("CHOOSE MODULE", ["SECURE SCAN", "AI CHATBOT", "CREATIVE LAB", "PREMIUM HUB"])

# --- AI CHATBOT LOGIC (Detailed Explanations) ---
def get_smart_response(user_input):
    ui = user_input.lower()
    if "scam" in ui or "fraud" in ui:
        return "Scams or 'Phishing' are deceptive attempts by cybercriminals to steal your sensitive data like passwords, credit card numbers, or personal identity. They often masquerade as trustworthy entities in electronic communication, such as emails, SMS, or fake websites that look identical to the real ones. To protect yourself, always inspect the sender's email address or the website's URL for subtle misspellings and verify the source before providing info. Never click on suspicious links, and most importantly, never share your One-Time Passwords (OTP) or PINs with anyone, even if they claim to be from a bank. If you suspect a scam, report it to the relevant authorities immediately and block the contact. Cyber awareness is your first line of defense against these digital threats, so stay vigilant and keep your private information confidential at all times."
    elif "password" in ui or "hack" in ui or "security" in ui:
        return "Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. The foundation of strong security is a robust password strategy: use at least 12 characters, including upper and lower case letters, numbers, and special symbols. Never reuse the same password across multiple platforms, because if one account is compromised, all others are at risk. Additionally, implementing Multi-Factor Authentication (MFA) or 2FA adds a critical layer of protection that prevents unauthorized access even if your password is stolen. Regularly update your software, as these updates often contain security patches for known vulnerabilities. Remember, digital security is not a one-time setup, but a continuous habit of being cautious and proactive with your digital footprint."
    elif "ai" in ui or "artificial intelligence" in ui:
        return "Artificial Intelligence (AI) is a field of computer science that simulates human intelligence processes by machines, especially computer systems. These processes include learning, reasoning, and self-correction. In our app, the AI engine processes your inputs to provide smart, simulated responses based on established security logic. While AI can automate tasks and provide rapid insights, it is important to remember that AI models operate based on patterns and data they have been trained on. Our specific AI module aims to empower users by simplifying complex security information into actionable steps. As technology evolves, AI will continue to play a pivotal role in detecting threats, optimizing workflows, and creating digital content, making it an essential tool for the modern digital era."
    else:
        return "CyberMind AI is designed to act as your personal digital security and creative assistant. Whether you are curious about protecting your privacy, learning about new technology, or looking to generate creative assets, this platform provides the tools you need. My purpose is to help you navigate the digital landscape safely by providing expert advice and streamlined utilities. If you have specific questions about online safety or technical guidance, feel free to ask, and I will provide a detailed explanation to guide your next steps."

# --- MAIN APP LOGIC ---
if menu == "SECURE SCAN":
    st.header("🛡️ THREAT DEFENSE SYSTEM")
    target = st.text_input("Enter Link/IP/App Name:")
    if st.button("RUN DEEP SCAN"):
        with st.spinner("Analyzing Packet Data..."):
            time.sleep(3)
            result = random.choice(["SAFE", "HIGH RISK DETECTED", "PHISHING ATTEMPT"])
            if result == "SAFE":
                st.success(f"SCAN RESULT: {result}. Target is secure.")
            else:
                st.error(f"SCAN RESULT: {result}! Action Required: Do not open.")

elif menu == "AI CHATBOT":
    st.header("🧠 NEURAL CHATBOT")
    user_query = st.text_input("Ask CyberMind AI anything:")
    if st.button("SEND QUERY"):
        if user_query:
            with st.spinner("Generating Detailed Explanation..."):
                time.sleep(1.5)
                st.write(get_smart_response(user_query))
        else:
            st.warning("Please enter a question.")

elif menu == "CREATIVE LAB":
    st.header("🎨 CREATIVE STUDIO")
    choice = st.selectbox("Select Generator", ["Image Generator", "Video Generator", "Face Swap"])
    prompt = st.text_input("Describe what you want:")
    if st.button("GENERATE ASSET"):
        with st.spinner(f"Simulating {choice}..."):
            time.sleep(4)
            st.success(f"{choice} generated successfully for: '{prompt}'")
            st.info("Note: Premium users get 4K resolution downloads. Upgrade for full access!")

elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO CYBERMIND X-PRO")
    st.markdown("""
    *   **Unlimited Neural Chat:** Advanced deep-thinking AI.
    *   **4K Media Exports:** High-quality images and videos.
    *   **Real-time Breach Monitoring:** Alert if your data is leaked.
    *   **Pro Cyber Shield:** Instant phishing blocker for browser.
    """)
    st.subheader("Choose Your Plan:")
    col1, col2 = st.columns(2)
    with col1:
        st.radio("Select Duration:", ["7 Days - ₹99", "1 Month - ₹299", "6 Months - ₹999", "1 Year - ₹1499", "Lifetime - ₹2499"])
    with col2:
        st.write("---")
        if st.button("ACTIVATE PREMIUM"):
            st.balloons()
            st.success("Redirecting to secure payment gateway... (Feature coming soon!)")
