import streamlit as st
import os
import sys

# --- Path Fix for Streamlit Cloud & Local ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# --- Safe Import ---
try:
    from ai_layer.forecast_ai import predict_tomorrow_revenue
except ModuleNotFoundError:
    st.error("❌ ai_layer module load nahi ho raha. Folder structure check karein.")
    st.stop()

# --- Dashboard Function ---
def admin_dashboard():
    st.set_page_config(page_title="Ultra ERP AI", layout="wide")
    st.title("🚀 Ultra ERP AI Dashboard")

    st.subheader("📊 Tomorrow Revenue Prediction")

    try:
        prediction = predict_tomorrow_revenue()
        st.success(f"💰 Expected Revenue: ₹ {prediction}")
    except Exception as e:
        st.error("AI Model Error:")
        st.code(str(e))
