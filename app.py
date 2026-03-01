import streamlit as st
from login import login_page
from dashboard import admin_dashboard

st.set_page_config(page_title="Raunak Ultra ERP AI", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    admin_dashboard()