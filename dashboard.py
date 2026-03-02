import streamlit as st
from ai_layer.forecast_ai import predict_tomorrow_revenue

def admin_dashboard():
    st.title("🚀 Raunak Ultra ERP AI Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("👥 Guests", "12")
    col2.metric("💰 Revenue", "₹ 18,450")
    col3.metric("⚠ Fraud Alerts", "0")

    st.markdown("---")

    st.subheader("🤖 AI Revenue Forecast")

    if st.button("Predict Tomorrow Revenue"):
        pred = predict_tomorrow_revenue()
        st.success(f"📈 Tomorrow Expected Revenue: ₹ {pred}")

    st.markdown("---")

    st.subheader("🧠 AI Modules Status")

    st.success("✔ Fraud Detection AI : READY")
    st.success("✔ Dynamic Pricing AI : READY")
    st.success("✔ Offer Generator AI : READY")
    st.success("✔ Staff Performance AI : READY")
    st.success("✔ Customer Retargeting AI : READY")
