import streamlit as st

def guests_page():
    st.title("🧾 Guest Entry System")

    name = st.text_input("Guest Name")
    mobile = st.text_input("Mobile Number")
    persons = st.number_input("No. of Persons", 1, 50, 1)
    amount = st.number_input("Bill Amount ₹", 0, 100000, 0)

    if st.button("Save Entry"):
        if name and mobile:
            st.success("✅ Guest Entry Saved Successfully")
        else:
            st.error("❌ Name & Mobile required")
