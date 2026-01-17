import streamlit as st


def render_product_card(product: dict, add_to_cart_fn=None):
    """Render product card with quantity tracker instead of buy button"""
    
    # Initialize session state for quantity if not exists
    quantity_key = f"quantity_{product['id']}"
    if quantity_key not in st.session_state:
        st.session_state[quantity_key] = 1

    with st.container():
        st.markdown(
            """
            <style>
            .product-card {
                border: 1px solid #e0e0e0;
                padding: 16px;
                border-radius: 10px;
                margin-bottom: 16px;
                background-color: #009668;
            }
            .quantity-controls {
                display: flex;
                gap: 10px;
                align-items: center;
                margin-top: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="product-card">
                <h4>{product['name']}</h4>
                <p style="color: #ffffff;">{product['description']}</p>
                <p><b>₹ {product['price']}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Quantity tracker with +/- buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button(" −1 ", key=f"dec_{product['id']}", use_container_width=True):
                if st.session_state[quantity_key] > 1:
                    st.session_state[quantity_key] -= 1
        
        with col2:
            st.write(f"Quantity: {st.session_state[quantity_key]}")
        
        with col3:
            if st.button(" +1 ", key=f"inc_{product['id']}", use_container_width=True):
                st.session_state[quantity_key] += 1

        # Add to cart button
        if st.button("Add to Cart", key=f"add_{product['id']}"):
            # Add to cart with quantity
            cart_item = {
                "product_id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "quantity": st.session_state[quantity_key]
            }
            
            if "cart" not in st.session_state:
                st.session_state["cart"] = []
            
            # Check if product already in cart
            existing_item = None
            for item in st.session_state["cart"]:
                if item["product_id"] == product["id"]:
                    existing_item = item
                    break
            
            if existing_item:
                existing_item["quantity"] += st.session_state[quantity_key]
            else:
                st.session_state["cart"].append(cart_item)
            
            st.success(f"Added {st.session_state[quantity_key]} to cart")
            st.session_state[quantity_key] = 1  # Reset quantity

