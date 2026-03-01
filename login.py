import streamlit as st

def login_page():
    st.title("🔐 Secure Login")

    users = {
        "admin": {"password": "1234", "role": "Admin"},
        "staff": {"password": "1234", "role": "Staff"}
    }

    username = st.selectbox("Select User", list(users.keys()))
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if password == users[username]["password"]:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.session_state.role = users[username]["role"]
            st.experimental_rerun()
        else:
            st.error("Invalid Password")