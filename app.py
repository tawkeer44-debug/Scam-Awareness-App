elif menu == "PREMIUM HUB":
    st.header("👑 UPGRADE TO CYBERMIND X-PRO")
    
    # 1. Feature Benefits Section
    st.subheader("🔥 UNLOCK EXCLUSIVE FEATURES")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("✅ **Unlimited Neural Chat** (No Limits)")
        st.markdown("✅ **4K Ultra-HD Generation** (Creative Lab)")
    with col2:
        st.markdown("✅ **Real-time Breach Alerts** (Active Protection)")
        st.markdown("✅ **Ad-Free Experience**")
    
    st.divider()
    
    # 2. Pricing Plans
    st.subheader("🚀 SELECT YOUR PLAN")
    plan = st.radio(
        "Choose the best plan for you:",
        [
            "7 Days Trial - $4.99",
            "6 Months Plan - $29.99",
            "1 Year Plan - $49.99",
            "Lifetime Access - $99.99"
        ]
    )
    
    # 3. Action Button
    if st.button("ACTIVATE PREMIUM NOW"):
        st.balloons()
        st.success(f"Processing payment for: {plan}")
        st.info("Redirecting to secure stripe/gateway... (Feature coming soon!)")
