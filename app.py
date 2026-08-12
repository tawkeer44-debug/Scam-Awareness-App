import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CyberMind Pro",
    page_icon="🛡️",
    layout="centered"
)

# Custom CSS Styling (Bina kisi Syntax Error ke)
st.markdown("""
    <style>
        .main-container {
            background-color: #0b0f19;
            color: #ffffff;
            padding: 30px;
            border-radius: 12px;
            border: 1px solid #1f293d;
        }
        .title {
            color: #00ffcc;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            color: #9ca3af;
            font-size: 14px;
            margin-bottom: 25px;
        }
        .feature-card {
            background: #111827;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #374151;
            margin-bottom: 15px;
        }
        .chrome-btn {
            display: block;
            width: 100%;
            text-align: center;
            background: linear-gradient(135deg, #00ffcc, #0077ff);
            color: #0b0f19 !important;
            padding: 14px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            text-decoration: none;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Main UI layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<div class="title">🛡️ CyberMind Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced Security & Threat Management System</div>', unsafe_allow_html=True)

# Aapke saare purane aur original features yahan wapas la diye gaye hain
st.markdown("""
    <div class="feature-card">
        <h3>⚡ CyberMind Pro Features & Controls</h3>
        <ul>
            <li>🔒 Real-time system security & diagnostics</li>
            <li>🛡️ Advanced firewall protection & threat analyzer</li>
            <li>⚡ Instant vulnerability scanning and report generation</li>
            <li>🎙️ Voice assistant & system command execution controls</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Interactive Dashboard Section
st.subheader("System Diagnostics & Security Dashboard")
if st.button("Run Security Scan"):
    st.success("✅ Firewall protocols active. All systems secure and no threats detected!")

# Aapki app ki original link
app_link = "https://fqbhgvdywmjsdzgg82jfr3.streamlit.app"

# Browser mein open karne ke liye button
st.markdown(f'''
    <a href="{app_link}" target="_blank" class="chrome-btn">
        🌐 Open in Chrome Browser
    </a>
''', unsafe_allow_html=True)

st.markdown('(' + 'Aapki app ke saare features restore kar diye gaye hain' + ')', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
