import streamlit as st
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

try:
    from ai_layer.forecast_ai import predict_tomorrow_revenue
except Exception as e:
    st.error(f"AI Module Load Error: {e}")
    st.stop()

def admin_dashboard():
    st.title("🚀 Ultra ERP AI Dashboard")

    revenue = predict_tomorrow_revenue()

    st.metric("📈 Tomorrow Revenue Prediction", f"₹ {revenue}")
