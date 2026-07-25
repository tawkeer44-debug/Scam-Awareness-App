import streamlit as st
import random
import datetime

# Economy Manager Class
class AppEconomy:
    def __init__(self):
        if 'coins' not in st.session_state: st.session_state.coins = 100
        if 'subscription' not in st.session_state: st.session_state.subscription = "Free"
        if 'reward_claimed' not in st.session_state: st.session_state.reward_claimed = False

    def add_coins(self, amount):
        st.session_state.coins += amount
        st.success(f"Added {amount} Coins! Total: {st.session_state.coins}")

    def claim_daily(self):
        if not st.session_state.reward_claimed:
            self.add_coins(50)
            st.session_state.reward_claimed = True
        else:
            st.warning("Daily reward already claimed today!")

    def upgrade_plan(self, plan_name, cost):
        if st.session_state.coins >= cost:
            st.session_state.coins -= cost
            st.session_state.subscription = plan_name
            st.success(f"Upgraded to {plan_name} successfully!")
        else:
            st.error("Not enough coins!")

# UI Implementation
st.title("💰 CyberMind Economy Hub")
eco = AppEconomy()

# Display Balance
st.metric("Your Balance", f"{st.session_state.coins} Coins")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎁 Claim Daily Reward"):
        eco.claim_daily()

with col2:
    st.write(f"Current Plan: **{st.session_state.subscription}**")

with col3:
    if st.button("🚀 Upgrade to Pro (Cost: 500)"):
        eco.upgrade_plan("Pro Member", 500)

# Referral Logic
st.subheader("🔗 Referral System")
st.write("Share your code: `CYBER_X_100`")
ref_code = st.text_input("Enter Friend's Referral Code:")
if st.button("Redeem Referral"):
    if ref_code == "CYBER_X_100":
        eco.add_coins(100)
    else:
        st.error("Invalid Code!")

# Monetization Info
st.info("💡 Tip: To implement real payments (Stripe/Razorpay) and Creator Monetization, you will need a backend database (Firebase or Supabase) to store user data permanently.")
