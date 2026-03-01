import streamlit as st
import sys
import os

# 🔥 ROOT PATH FIX
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from ai_layer.forecast_ai import predict_tomorrow_revenue

def admin_dashboard():
    st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

    st.title("📊 Raunak Ultra ERP AI Dashboard")

    revenue = st.number_input("Today's Total Revenue", min_value=0.0, step=100.0)

    if st.button("Predict Tomorrow Revenue"):
        prediction = predict_tomorrow_revenue(revenue)
        st.success(f"🔥 Tomorrow Predicted Revenue: ₹ {prediction:,.2f}")
