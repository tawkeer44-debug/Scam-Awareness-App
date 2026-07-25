import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="CyberMind X Pro", layout="wide")

# --- INITIALIZE STATE ---
if 'coins' not in st.session_state: st.session_state.coins = 100
if 'is_pro' not in st.session_state: st.session_state.is_pro = False
if 'output' not in st.session_state: st.session_state.output = "" # Output save karne ke liye

# --- STYLING ---
st.markdown("<style>.stApp { background-color: #000; color: #00ff41; font-family: 'Courier New'; }</style>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("💀 COMMAND CENTER")
menu = st.sidebar.selectbox("MENU", ["DASHBOARD", "SECURITY LAB", "PRO SUITE", "PREMIUM HUB", "REFERRAL"])

# --- DASHBOARD ---
if menu == "DASHBOARD":
    st.title("⚡ DASHBOARD")
    if 'claimed' not in st.session_state: st.session_state.claimed = False
    
    if not st.session_state.claimed:
        if st.button("CLAIM DAILY 100"):
            st.session_state.coins += 100
            st.session_state.claimed = True
            st.rerun()
    else:
        st.write("✅ Daily reward already claimed.")

# --- SECURITY LAB (Output Fix) ---
elif menu == "SECURITY LAB":
    st.header("🛡️ SECURITY LAB")
    cmd = st.text_input("Enter Command:", "scan --phishing")
    if st.button("SUBMIT"):
        st.session_state.output = f"[+] Running {cmd}...\n[+] Analyzing...\n[+] Result: System Secure.\n[+] Credits Added."
        st.session_state.coins += 10
    st.code(st.session_state.output)

# --- PREMIUM HUB (Subscription Model) ---
elif menu == "PREMIUM HUB":
    st.header("💎 PREMIUM PLANS")
    plans = {
        "7 Days": "$5", "1 Month": "$15", "30 Days": "$15", 
        "6 Months": "$60", "1 Year": "$100", "Lifetime": "$200"
    }
    for plan, price in plans.items():
        if st.button(f"Buy {plan} for {price}"):
            st.success(f"Redirecting to payment for {plan}...")

# --- REFERRAL LOGIC (Real Join) ---
elif menu == "REFERRAL":
    st.header("🔗 REFERRAL HUB")
    st.write("Get 100 coins only when 15 friends JOIN the app!")
    st.write(f"Friends Joined: {st.session_state.get('joined', 0)}/15")
    
    # Simulate real join
    if st.button("Simulate Friend Joining"):
        joined = st.session_state.get('joined', 0) + 1
        st.session_state.joined = joined
        if joined == 15:
            st.session_state.coins += 100
            st.success("Milestone Reached! 100 Coins Added.")
            st.session_state.joined = 0 # Reset
        st.rerun()
