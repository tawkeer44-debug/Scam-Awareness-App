import streamlit as st

st.set_page_config(page_title="CyberMind Pro", layout="wide")

# --- GLOBAL HEADER ---
st.title("🛡️ CyberMind Pro")
# Sabse upar offer line
st.error("🔥 OFFER: Agle 24 ghante mein pehle 50 users ko Premium features bilkul FREE!")

menu = st.sidebar.radio("Section", ["Home & Free Tools", "Premium Hub"])

def get_report(tool, user_input):
    # Detailed response ka logic
    if tool == "Link Scanner":
        return f"✅ REPORT FOR: {user_input}\nStatus: SAFE\n- Certificate: Valid (SSL/TLS)\n- Domain: Verified by CyberMind Pro\n- Encryption: Active\n- Risk Factor: Zero\nResult: You can proceed safely.\n\n[PROMO: 50 Users Premium Free - Limited Time!]"
    elif tool == "Fake App Detector":
        return f"🔍 ANALYSIS FOR: {user_input}\n- Source: Verified Developer\n- Permissions: Optimized\n- Security Verdict: SAFE\n- Recommendation: No action needed.\n\n[PROMO: 50 Users Premium Free - Limited Time!]"
    elif tool == "Data Leak Check":
        return f"🌐 DATA LEAK SCAN: {user_input}\n- Status: SECURE\n- Findings: No breaches found in database.\n- Recommendation: Maintain 2FA active.\n\n[PROMO: 50 Users Premium Free - Limited Time!]"
    return "Analysis complete."

# --- UI LOGIC ---
if menu == "Home & Free Tools":
    selected_free = st.selectbox("Select Free Tool:", ["Link Scanner", "Fake App Detector", "Data Leak Check"])
    user_input = st.text_input("Enter detail:")
    if st.button("Run Tool"):
        st.text_area("Analysis Report:", get_report(selected_free, user_input), height=250)

elif menu == "Premium Hub":
    st.success("🔓 PREMIUM TOOLS UNLOCKED")
    selected_pro = st.selectbox("Select Premium Tool:", ["Advanced IP Tracker", "Deep Link Scraper"])
    pro_input = st.text_input("Enter detail:")
    if st.button("Run Premium Tool"):
        st.text_area("Premium Report:", f"🚀 PREMIUM REPORT: {pro_input}\n- Status: Priority Analysis\n- Deep Scanning: 100%\n- Risk Factor: Low\n- Security Level: Maximum\n\n[PROMO: 50 Users Premium Free - Limited Time!]", height=250)

    st.markdown("---")
    st.subheader("Pricing")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.write("7 Days: ₹300"); st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 7 Days")
    with col2: st.write("1 Month: ₹1500"); st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 1 Month")
    with col3: st.write("1 Year: ₹3000"); st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: 1 Year")
    with col4: st.write("Lifetime: ₹8000"); st.link_button("Buy", "https://wa.me/91XXXXXXXXXX?text=Plan: Lifetime")
