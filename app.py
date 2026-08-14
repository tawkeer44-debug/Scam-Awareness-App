import streamlit as st

INSTAGRAM_URL = "https://www.instagram.com/th3_tawkeer/"

plans = [
    ("7 Days Trial", "$0"),
    ("1 Month", "$4.99"),
    ("3 Months", "$12.99"),
    ("6 Months", "$22.99"),
    ("9 Months", "$31.99"),
    ("1 Year", "$39.99"),
    ("2 Years", "$69.99"),
    ("4 Years", "$119.99"),
    ("Lifetime", "$199.99"),
]

st.title("💎 CyberMind Pro Premium Hub")

cols = st.columns(3)

for i, (plan, price) in enumerate(plans):
    with cols[i % 3]:
        st.markdown(f"""
### {plan}

**Price:** {price}

✅ Premium Dashboard  
✅ AI Security Tools  
✅ Dark Web Scanner  
✅ AI Assistant  
✅ Premium Updates
""")

        st.link_button(
            "📩 Buy via Instagram",
            INSTAGRAM_URL
        )
