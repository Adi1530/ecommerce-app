import streamlit as st

from frontend.api import login, register
from frontend.auth import save_session


def render():
    st.title("Ecommerce")

    tab1, tab2 = st.tabs(["Register", "Login"])

    with tab1:
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")

        if st.button("Register"):
            r = register(email, password)

            if r.status_code == 201:
                st.success("Registered successfully. Please login.")
            else:
                try:
                    data = r.json()
                    st.error(data.get("detail", "Registration failed"))
                except ValueError:
                    st.error(f"Registration failed ({r.status_code})")

    with tab2:
        email = st.text_input("Login Email", key="log_email")
        password = st.text_input("Login Password", type="password", key="log_pass")

        if st.button("Login"):
            r = login(email, password)

            if r.status_code == 200:
                save_session(r.json()["access_token"])
                st.success("Login successful")
                st.rerun()
            else:
                try:
                    data = r.json()
                    st.error(data.get("detail", "Invalid credentials"))
                except ValueError:
                    st.error(f"Login failed ({r.status_code})")
