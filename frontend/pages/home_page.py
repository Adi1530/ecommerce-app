import streamlit as st

from ..api import add_to_cart, get_products
from ..components.product_card import render_product_card


def render():
    st.subheader("Products")

    r = get_products()
    if r.status_code != 200:
        st.error("Failed to load products")
        return

    products = r.json()
    # cols = st.columns(5)

    for i, product in enumerate(products):
        render_product_card(product, add_to_cart)
        # st.title("")
