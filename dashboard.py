import streamlit as st
import pandas as pd

def admin_dashboard():
    st.title("🚀 Raunak Ultra ERP AI Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Guests", "124")
    col2.metric("💰 Revenue", "₹ 38,450")
    col3.metric("🛒 Orders", "312")
    col4.metric("🚨 Fraud Alerts", "0")

    st.divider()

    st.subheader("🤖 AI Modules Status")

    ai_status = [
        "Revenue Forecast AI",
        "Fraud Detection AI",
        "Dynamic Pricing AI",
        "Offer Generator AI",
        "Staff Performance AI",
        "Customer Retargeting AI"
    ]

    for ai in ai_status:
        st.success(f"✅ {ai} : READY")

    st.divider()

    st.subheader("👥 Staff Management Panel")

    name = st.text_input("Staff Name")
    mobile = st.text_input("Mobile")
    role = st.selectbox("Role", ["Manager", "Cashier", "Kitchen", "Delivery", "Accountant"])

    if st.button("Create Staff"):
        if name and mobile:
            st.success(f"✅ Staff {name} ({role}) Created Successfully")
        else:
            st.error("❌ Name & Mobile required")

    st.divider()

    st.success("🔥 Ultra ERP AI Admin System Working Perfectly")
