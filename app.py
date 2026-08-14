import streamlit as st
import plotly.express as px
import pandas as pd
import random

st.set_page_config(
    page_title="CyberMind Pro",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
background:#070b14;
color:white;
}
.block-container{
padding-top:1rem;
}
.card{
background:#101827;
padding:20px;
border-radius:15px;
border:1px solid #1f3b63;
text-align:center;
box-shadow:0 0 20px rgba(0,255,255,.15);
}
.title{
font-size:40px;
font-weight:bold;
color:#00ffe5;
}
</style>
""",unsafe_allow_html=True)

st.sidebar.title("🛡 CyberMind Pro")
st.sidebar.success("AI Security Dashboard")

menu=st.sidebar.radio("Navigation",
[
"Dashboard",
"AI Scam Detector",
"Password Leak",
"Dark Web",
"AI Terminal"
])

if menu=="Dashboard":

    st.markdown("<div class='title'>CyberMind Pro Live Dashboard</div>",unsafe_allow_html=True)

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.markdown(f"<div class='card'><h3>👥 Live Users</h3><h2>{9995+random.randint(0,20)}</h2></div>",unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'><h3>🛡 Security</h3><h2>99.9%</h2></div>",unsafe_allow_html=True)

    with c3:
        st.markdown(f"<div class='card'><h3>🚨 Threats Blocked</h3><h2>{1240+random.randint(0,50)}</h2></div>",unsafe_allow_html=True)

    with c4:
        st.markdown("<div class='card'><h3>🤖 AI Status</h3><h2>ONLINE</h2></div>",unsafe_allow_html=True)

    st.write("")

    df=pd.DataFrame({
        "Time":list(range(24)),
        "Threats":[random.randint(10,100) for i in range(24)]
    })

    fig=px.line(df,x="Time",y="Threats",template="plotly_dark")
    st.plotly_chart(fig,use_container_width=True)

    st.subheader("🌍 Live Threat Feed")

    data=pd.DataFrame({
        "Country":["India","USA","Germany","Brazil","Japan"],
        "Threat":["Malware","Phishing","Botnet","DDoS","Exploit"],
        "Status":["Blocked"]*5
    })

    st.dataframe(data,use_container_width=True)

    st.subheader("🤖 CyberMind AI")

    prompt=st.text_input("Ask AI")

    if prompt:
        st.success("CyberMind AI Response")
        st.write("Your system appears secure. Continue regular scanning.")

elif menu=="AI Scam Detector":
    st.title("AI Scam Detector")
    msg=st.text_area("Paste message")
    if st.button("Analyze"):
        st.success("No High Risk Scam Detected")

elif menu=="Password Leak":
    st.title("Password Leak Checker")
    email=st.text_input("Email")
    if st.button("Check"):
        st.info("No leak found.")

elif menu=="Dark Web":
    st.title("Dark Web Scanner")
    domain=st.text_input("Domain")
    if st.button("Scan"):
        st.success("Nothing suspicious detected.")

elif menu=="AI Terminal":
    st.title("Cyber Terminal")
    cmd=st.text_input("Command")
    if cmd:
        st.code(f"> {cmd}\nExecuted Successfully")
