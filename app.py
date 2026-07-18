elif choice == "💎 Premium Upgrade":
    st.title("💎 CyberMind Pro | Pro Dashboard")
    st.write("---")
    
    # 8 Premium Features in a Clean Grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🛠️ Pro Security Tools")
        st.success("📁 Deep File & PDF Analyzer")
        st.success("🔔 Real-Time Scam Alerts")
        st.success("🔒 Encrypted Cloud Storage")
        st.success("🤖 Hindi/Regional AI Peter")
        
    with col2:
        st.markdown("### 🚀 Exclusive Perks")
        st.success("🚫 Zero Ad Experience")
        st.success("⚡ Priority Support (24/7)")
        st.success("🛡️ Advanced Device Tracker")
        st.success("📊 Monthly Security Reports")

    st.write("---")
    st.subheader("Select Your Subscription")
    
    # Pricing Layout
    p1, p2, p3, p4 = st.columns(4)
    with p1: st.link_button("7 Days - ₹49", "YOUR_LINK")
    with p2: st.link_button("Monthly - ₹199", "YOUR_LINK")
    with p3: st.link_button("Yearly - ₹999", "YOUR_LINK")
    with p4: st.link_button("Lifetime - ₹2499", "YOUR_LINK")
    
    st.info("Payment ke baad, apni Transaction ID humein email karein: support@cybermind.com")
