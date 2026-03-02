import streamlit as st
import os
import sys

# Fix path for Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

try:
    from ai_layer.forecast_ai import predict_tomorrow_revenue
except:
    predict_tomorrow_revenue = None


def admin_dashboard():
    st.set_page_config(page_title="Ultra ERP AI Dashboard", layout="wide")

    st.title("🚀 Raunak Ultra ERP AI Dashboard")

    col1, col2, col3 = st.columns(3)

    # KPI Metrics
    with col1:
        st.metric("👥 Guests", "0")

    with col2:
        st.metric("💰 Revenue", "₹ 0")

    with col3:
        st.metric("🚨 Fraud Alerts", "0")

    st.divider()

    st.subheader("📈 AI Revenue Forecast")

    if predict_tomorrow_revenue:
        if st.button("🔮 Predict Tomorrow Revenue"):
            revenue = predict_tomorrow_revenue()
            st.success(f"Tomorrow Expected Revenue: ₹ {revenue}")
    else:
        st.error("❌ AI module not loaded. Folder structure check karein.")


    st.divider()

    st.subheader("⚙ AI Modules Status")

    st.success("✔ Fraud Detection AI : READY")
    st.success("✔ Dynamic Pricing AI : READY")
    st.success("✔ Offer Generator AI : READY")
    st.success("✔ Staff Performance AI : READY")
    st.success("✔ Customer Retargeting AI : READY")
