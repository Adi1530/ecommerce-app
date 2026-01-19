import streamlit as st

from frontend.api import checkout


def render():
    st.subheader("Shopping Cart")

    # Initialize cart if not exists
    if "cart" not in st.session_state:
        st.session_state["cart"] = []

    if not st.session_state["cart"]:
        st.info("Your cart is empty")
        return

    st.write("### Your Items")

    total_amount = 0
    cart_data = []

    for item in st.session_state["cart"]:
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.write(item["name"])

        with col2:
            st.write(f"₹{item['price']}")

        with col3:
            st.write(f"Qty: {item['quantity']}")

        item_total = item["price"] * item["quantity"]
        with col4:
            st.write(f"₹{item_total}")

        with col5:
            if st.button("Remove", key=f"remove_{item['product_id']}"):
                st.session_state["cart"].remove(item)
                st.rerun()

        total_amount += item_total
        cart_data.append(
            {
                "product_id": item["product_id"],
                "quantity": item["quantity"],
                "price": item["price"],
            }
        )

    # Divider
    st.divider()

    # Display total
    st.markdown(f"### **Total Amount: ₹{total_amount}**")

    # Checkout form
    st.write("### Delivery Address")
    address = st.text_area("Enter your delivery address", height=100)

    if st.button("Checkout", type="primary"):
        if not address.strip():
            st.error("Please enter delivery address")
            return

        response = checkout(cart_data, address, total_amount)

        if response.status_code == 200:
            st.success("Order placed successfully!")
            st.session_state["cart"] = []
            st.session_state["page"] = "home"
            st.rerun()
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
