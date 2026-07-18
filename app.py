elif choice == "Premium Features":
    st.title("💎 CyberMind Pro Advanced Suite")
    st.write("Apni security ko premium level par le jayein.")

    # Pricing Table Layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**7 Days**")
        st.subheader("₹49")
        if st.button("Buy 7 Days"):
            st.write("Redirecting to payment...")

    with col2:
        st.markdown("**Monthly**")
        st.subheader("₹199")
        if st.button("Buy Monthly"):
            st.write("Redirecting to payment...")

    with col3:
        st.markdown("**Yearly**")
        st.subheader("₹999")
        if st.button("Buy Yearly"):
            st.write("Redirecting to payment...")

    with col4:
        st.markdown("**Lifetime**")
        st.subheader("₹2499")
        if st.button("Buy Lifetime"):
            st.write("Redirecting to payment...")

    st.info("Payment ke liye hum Razorpay ka use karte hain. Sabse safe aur secure.")
