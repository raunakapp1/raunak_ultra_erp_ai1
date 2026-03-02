import streamlit as st
from login import login_page
from dashboard import admin_dashboard
from core_app.guests_engine import guests_page

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

# Session init
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.role = None

# Login flow
if not st.session_state.login:
    login_page()
    st.stop()

# Sidebar
st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio("Go To", ["Dashboard", "Guest Entry"])

st.sidebar.markdown("---")

if st.sidebar.button("🔓 Logout"):
    st.session_state.login = False
    st.experimental_rerun()

# Routing
if page == "Dashboard":
    admin_dashboard()
elif page == "Guest Entry":
    guests_page()
