import streamlit as st
import sys
import os

# Root folder ko python path me add karo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from ai_layer.forecast_ai import predict_tomorrow_revenue


def admin_dashboard():
    st.title("🚀 Ultra ERP AI Dashboard")

    revenue = predict_tomorrow_revenue()

    st.metric("📈 Tomorrow Revenue Prediction", f"₹ {revenue}")
