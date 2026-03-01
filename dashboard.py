import streamlit as st
import os
import importlib.util

# ---------- DYNAMIC MODULE LOADER ----------
def load_module(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

forecast_ai = load_module(
    os.path.join(BASE_DIR, "ai_layer", "forecast_ai.py"),
    "forecast_ai"
)

predict_tomorrow_revenue = forecast_ai.predict_tomorrow_revenue

# ---------- DASHBOARD ----------
def admin_dashboard():
    st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

    st.title("📊 Raunak Ultra ERP AI Dashboard")

    revenue = st.number_input("Today's Revenue ₹", min_value=0.0, step=100.0)

    if st.button("Predict Tomorrow Revenue"):
        prediction = predict_tomorrow_revenue(revenue)
        st.success(f"🔥 Tomorrow Predicted Revenue: ₹ {prediction:,.2f}")
