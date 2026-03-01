import streamlit as st
from ai_layer.forecast_ai import predict_tomorrow_revenue
from ai_layer.pricing_ai import dynamic_price
from ai_layer.offer_ai import generate_offer
from ai_layer.staff_ai import staff_score
from ai_layer.retarget_ai import campaign_plan

def admin_dashboard():
    st.title("📊 Raunak Ultra ERP AI Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        revenue = st.number_input("Today's Revenue ₹", min_value=0)
        if st.button("Predict Tomorrow Revenue"):
            pred = predict_tomorrow_revenue(revenue)
            st.success(f"Tomorrow Expected: ₹ {pred}")

    with col2:
        base_price = st.number_input("Base Item Price ₹", min_value=10)
        demand = st.slider("Demand Level",1,10)
        if st.button("Dynamic Price"):
            price = dynamic_price(base_price, demand)
            st.success(f"Optimized Price: ₹ {price}")

    with col3:
        festival = st.selectbox("Festival", ["Holi","Diwali","New Year","Christmas"])
        if st.button("Generate Offer"):
            offer = generate_offer(festival)
            st.info(offer)

    st.divider()

    st.subheader("🧑‍💼 Staff Performance AI")
    staff_name = st.text_input("Staff Name")
    sales = st.number_input("Sales ₹",min_value=0)
    if st.button("Analyze Staff"):
        score = staff_score(sales)
        st.success(f"{staff_name} Performance Score: {score}/100")

    st.divider()

    st.subheader("📲 Customer Retarget AI")
    total_customers = st.number_input("Total Customers", min_value=0)
    if st.button("Generate Campaign Plan"):
        plan = campaign_plan(total_customers)
        st.info(plan)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()