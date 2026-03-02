import streamlit as st
import pandas as pd

# ---------- Dummy Database ----------
if "staff_db" not in st.session_state:
    st.session_state.staff_db = []

# ---------- DASHBOARD ----------
def admin_dashboard():
    st.title("🚀 Raunak Ultra ERP AI Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Guests", "124")
    col2.metric("💰 Revenue", "₹ 38,450")
    col3.metric("🛒 Orders", "312")
    col4.metric("🚨 Fraud Alerts", "0")

    st.divider()

    # ---------- AI MODULE STATUS ----------
    st.subheader("🤖 AI Modules Status")

    ai_status = {
        "Revenue Forecast AI": "READY",
        "Fraud Detection AI": "READY",
        "Dynamic Pricing AI": "READY",
        "Offer Generator AI": "READY",
        "Staff Performance AI": "READY",
        "Customer Retargeting AI": "READY"
    }

    for k, v in ai_status.items():
        st.success(f"✅ {k} : {v}")

    st.divider()

    # ---------- STAFF MANAGEMENT ----------
    st.subheader("👥 Staff Management Panel")

    with st.expander("➕ Create New Staff"):
        name = st.text_input("Staff Name")
        mobile = st.text_input("Mobile Number")
        role = st.selectbox("Role", ["Manager", "Cashier", "Kitchen", "Delivery", "Accountant"])

        permissions = st.multiselect("Permissions", [
            "Dashboard View",
            "Guest Entry",
            "Billing",
            "Inventory",
            "Reports",
            "Staff Management"
        ])

        if st.button("Create Staff"):
            if name and mobile:
                st.session_state.staff_db.append({
                    "Name": name,
                    "Mobile": mobile,
                    "Role": role,
                    "Permissions": ", ".join(permissions)
                })
                st.success("✅ Staff Created Successfully")
            else:
                st.error("❌ Name & Mobile Required")

    st.divider()

    # ---------- STAFF LIST ----------
    st.subheader("📋 Staff Database")

    if st.session_state.staff_db:
        df = pd.DataFrame(st.session_state.staff_db)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("⚠ No Staff Created Yet")

    st.divider()

    # ---------- ACCESS CONTROL ----------
    st.subheader("🔐 Role Access Control")

    st.info("""
    Admin → Full Access  
    Manager → Dashboard + Reports + Staff View  
    Cashier → Billing + Guest Entry  
    Kitchen → Orders Only  
    Delivery → Delivery Panel  
    Accountant → Reports + GST + Finance  
    """)

    st.divider()

    # ---------- SYSTEM CONTROL ----------
    st.subheader("⚙ System Control Panel")

    col1, col2, col3 = st.columns(3)

    if col1.button("🔄 Restart System"):
        st.success("System Restarted")

    if col2.button("📤 Export Data"):
        st.success("Data Exported")

    if col3.button("🧹 Clear Cache"):
        st.success("Cache Cleared")

    st.divider()

    st.success("🔥 Ultra ERP AI Admin System Running Perfectly")
