elif menu == "PUBLIC WIFI LOCATOR":
    st.header("🌐 FREE PUBLIC WIFI LOCATOR")
    st.write("Help people find free, legal internet access near them.")
    
    # List of common free public wifi locations
    locations = {
        "Railway Station": "Platform 1, Waiting Room (Free for 30 min)",
        "City Central Library": "Free Public WiFi - Connected automatically",
        "Public Park (Sector 5)": "Govt-Free-WiFi (No password required)",
        "Community Center": "Public-Access-Wifi (Open Network)"
    }
    
    city = st.selectbox("Select your city area:", ["Main City", "North District", "Metro Station"])
    
    if st.button("FIND FREE ACCESS"):
        st.subheader("Available Free Zones:")
        for place, info in locations.items():
            st.success(f"📍 {place}: {info}")
        st.info("Note: Always use a VPN on public networks for your safety.")
