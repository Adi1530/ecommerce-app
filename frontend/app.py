import streamlit as st
from auth import logout
from pages import auth_page, home_page, checkout_page, admin_page

st.set_page_config(page_title="Ecommerce", layout="wide")

if "page" not in st.session_state:
    st.session_state["page"] = "auth"

if "token" in st.session_state:
    st.sidebar.write(f"{st.session_state['user']['email']}")
    st.sidebar.write(f"Role: {st.session_state['user']['role']}")
    st.sidebar.divider()

    # Navigation for regular users
    if st.session_state['user']['role'] == "USER":
        if st.sidebar.button("Home"):
            st.session_state["page"] = "home"

        # Cart indicator
        cart_count = len(st.session_state.get("cart", []))
        if st.sidebar.button(f"Checkout ({cart_count})"):
            st.session_state["page"] = "checkout"

    # Navigation for admin
    elif st.session_state['user']['role'] == "ADMIN":
        if st.sidebar.button("Orders Dashboard"):
            st.session_state["page"] = "admin"

        if st.sidebar.button("Products"):
            st.session_state["page"] = "home"

    if st.sidebar.button("Logout"):
        logout()

page = st.session_state["page"]

if page == "auth":
    auth_page.render()
elif page == "home":
    home_page.render()
elif page == "checkout":
    checkout_page.render()
elif page == "admin":
    admin_page.render()

