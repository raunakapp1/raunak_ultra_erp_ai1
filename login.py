import streamlit as st

def login_page():
    st.title("🔐 Login")

    users = {
        "admin": {"password": "admin123", "role": "admin"},
        "staff1": {"password": "1234", "role": "staff"},
        "staff2": {"password": "1234", "role": "staff"}
    }

    username = st.selectbox("Select User", list(users.keys()))
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if users[username]["password"] == password:
            st.session_state.login = True
            st.session_state.role = users[username]["role"]
            st.success("Login Successful")
            st.experimental_rerun()
        else:
            st.error("Wrong Password")
