import streamlit as st
import random

# --- ECONOMY LOGIC ---
def init_session():
    defaults = {
        'coins': 100,
        'level': 'Beginner',
        'sub_status': 'Free',
        'ref_bonus': False
    }
    for key, val in defaults.items():
        if key not in st.session_state: st.session_state[key] = val

init_session()

# --- SIDEBAR MONETIZATION ---
st.sidebar.title("💎 PRO ECONOMY")
st.sidebar.metric("Balance", f"{st.session_state.coins} 🪙")

menu = st.sidebar.radio("Economy Menu", ["Dashboard", "Earn Coins", "Subscription", "Creator Shop"])

# --- DASHBOARD ---
if menu == "Dashboard":
    st.title("📊 User Dashboard")
    st.write(f"Current Rank: **{st.session_state.level}**")
    st.write(f"Status: **{st.session_state.sub_status}**")
    
    if st.button("Daily Reward 🎁"):
        st.session_state.coins += 50
        st.success("Collected 50 Daily Coins!")

# --- EARN COINS (Referral & Ads) ---
elif menu == "Earn Coins":
    st.title("💸 Earn & Affiliate")
    ref = st.text_input("Enter Referral Code")
    if st.button("Apply Referral"):
        if ref == "CYBER2026":
            st.session_state.coins += 200
            st.success("Referral Applied!")
        else:
            st.error("Invalid Code")
            
    st.info("Watch Ad for 10 Coins (Simulated)")
    if st.button("Watch Video Ad"):
        st.session_state.coins += 10
        st.balloons()

# --- SUBSCRIPTION & PAID CONTENT ---
elif menu == "Subscription":
    st.title("👑 Premium Plans")
    plans = {"Basic (1 Month)": 500, "Pro (Lifetime)": 2000}
    
    for plan, cost in plans.items():
        if st.button(f"Buy {plan} for {cost} Coins"):
            if st.session_state.coins >= cost:
                st.session_state.coins -= cost
                st.session_state.sub_status = plan
                st.success(f"Purchased {plan}!")
            else:
                st.error("Insufficient Coins!")

# --- CREATOR SHOP (Monetization) ---
elif menu == "Creator Shop":
    st.title("🛒 Creator Assets")
    st.write("Buy Premium Scripts & Plugins")
    items = {"Hacker Theme Pack": 300, "Advanced Scanner Script": 800}
    
    for item, price in items.items():
        if st.button(f"Unlock {item} ({price} Coins)"):
            st.warning(f"Feature: {item} unlocked for your account.")
