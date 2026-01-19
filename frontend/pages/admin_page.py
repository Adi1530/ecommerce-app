import streamlit as st

from ..api import get_all_orders


def render():
    st.subheader("Admin Dashboard - Orders")

    response = get_all_orders()

    if response.status_code != 200:
        st.error("Failed to load orders")
        return

    orders = response.json()

    if not orders:
        st.info("No orders to dispatch")
        return

    st.write(f"### Total Orders: {len(orders)}")
    st.divider()

    for order in orders:
        with st.container():
            st.markdown(
                """
                <style>
                .order-card {
                    border: 1px solid #e0e0e0;
                    padding: 16px;
                    border-radius: 10px;
                    margin-bottom: 16px;
                    background-color: #009668;
                    color: white !important;
                }
                .order-card h4 {
                    color: black !important;
                }
                .order-card * {
                    color: black !important;
                }
                .order-row {
                    display: grid;
                    grid-template-columns: 1fr 1fr 1fr 1fr;
                    gap: 16px;
                    margin-bottom: 10px;
                    padding: 10px;
                    background-color: #009768;
                    border-radius: 5px;
                }
                .order-field {
                    padding: 8px;
                    color: black !important;
                }
                .order-label {
                    font-weight: bold;
                    color: black !important;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="order-card">
                    <h4 class="order-id">Order ID: {order['id']}</h4>
                    <div class="order-row">
                        <div class="order-field">
                            <span class="order-label">User ID:</span> {order['user_id']}
                        </div>
                        <div class="order-field">
                            <span class="order-label">Product ID:</span> {order['product_id']}
                        </div>
                        <div class="order-field">
                            <span class="order-label">Quantity:</span> {order['quantity']}
                        </div>
                        <div class="order-field">
                            <span class="order-label">Amount:</span> ₹{order['total_amount']}
                        </div>
                    </div>
                    <div class="order-row">
                        <div class="order-field">
                            <span class="order-label">Address:</span> {order['address']}
                        </div>
                        <div class="order-field">
                            <span class="order-label">Date:</span> {order['created_at'][:10]}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Mark as Dispatched", key=f"dispatch_{order['id']}"):
                    st.success(f"Order {order['id']} marked as dispatched")

            with col2:
                if st.button("View Details", key=f"details_{order['id']}"):
                    st.info(
                        f"Order Details:\n- User: {order['user_id']}\n- Products: {order['product_id']}\n- Address: {order['address']}"
                    )

        st.divider()
