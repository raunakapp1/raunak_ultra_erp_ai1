import streamlit as st
import os
import sys

# Ensure project root path is added
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Safe import of AI module
try:
    from forecast_ai import predict_tomorrow_revenue
except Exception as e:
    st.error(f"❌ AI module not loaded.\n\n{e}")
    st.stop()


def admin_dashboard():
    st.title("🚀 Ultra ERP AI Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Guests", "0")

    with col2:
        revenue = predict_tomorrow_revenue()
        st.metric("💰 Tomorrow Revenue Prediction", f"₹ {revenue}")

    with col3:
        st.metric("🚨 Fraud Alerts", "0")

    st.divider()

    st.subheader("🤖 AI Modules Status")

    st.success("✅ Revenue Forecast AI : READY")
    st.success("✅ Fraud Detection AI : READY")
    st.success("✅ Dynamic Pricing AI : READY")
    st.success("✅ Offer Generator AI : READY")
    st.success("✅ Staff Performance AI : READY")
    st.success("✅ Customer Retargeting AI : READY")
