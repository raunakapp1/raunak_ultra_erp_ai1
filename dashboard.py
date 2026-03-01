import streamlit as st
from ai_layer.forecast_ai import predict_tomorrow_revenue

def admin_dashboard():
    st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

    st.title("📊 Raunak Ultra ERP AI Dashboard")

    revenue = st.number_input("Today's Total Revenue", min_value=0.0, step=100.0)

    if st.button("Predict Tomorrow Revenue"):
        result = predict_tomorrow_revenue(revenue)
        st.success(f"🔥 Tomorrow Expected Revenue: ₹ {result:,.2f}")
