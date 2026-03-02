import streamlit as st
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

try:
    from ai_layer.forecast_ai import predict_tomorrow_revenue
    AI_STATUS = "✅ AI Module Loaded Successfully"
except Exception as e:
    AI_STATUS = f"❌ AI Load Error: {e}"


def admin_dashboard():
    st.title("🚀 Ultra ERP AI Dashboard")

    st.info(AI_STATUS)

    if "❌" not in AI_STATUS:
        revenue = predict_tomorrow_revenue()
        st.metric("📈 Tomorrow Revenue Prediction", f"₹ {revenue}")
    else:
        st.error("AI Module Load nahi ho raha – folder structure check karein")
