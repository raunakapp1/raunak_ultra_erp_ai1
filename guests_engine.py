import streamlit as st

def guests_page():
    st.title("🧾 Guest Entry System")

    col1, col2 = st.columns(2)

    name = col1.text_input("Guest Name")
    phone = col2.text_input("Mobile Number")

    category = st.selectbox("Category", [
        "Direct Walkin", "Swiggy", "Zomato", "EazyDiner",
        "VIP", "Party", "Corporate", "Other"
    ])

    pax = st.number_input("No of Pax", 1, 50, 2)

    if st.button("Save Entry"):
        st.success("✅ Guest Entry Saved Successfully")
