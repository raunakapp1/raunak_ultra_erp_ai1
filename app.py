import streamlit as st
from core_app.dashboard import admin_dashboard
from core_app.guests_engine import guests_page

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

st.sidebar.title("🚀 Ultra ERP AI")

menu = st.sidebar.radio("Navigation", ["Dashboard", "Guest Entry"])

if menu == "Dashboard":
    admin_dashboard()

elif menu == "Guest Entry":
    guests_page()
