import streamlit as st

def guests_page():
    st.title("👥 Guest Entry System")

    with st.form("guest_form"):
        name = st.text_input("Customer Name")
        mobile = st.text_input("Mobile Number")
        persons = st.number_input("Total Persons", 1, 50)
        source = st.selectbox("Order Source", ["Walk-in", "Zomato", "Swiggy", "Dine-in", "Takeaway"])

        submitted = st.form_submit_button("Save Entry")

        if submitted:
            st.success("✅ Guest Entry Saved Successfully")

    st.info("📊 This data will feed Revenue AI + Retarget AI + Offer AI")
