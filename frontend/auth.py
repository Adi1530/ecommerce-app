import streamlit as st
import jwt

def save_session(token: str):
    st.session_state["token"] = token
    payload = jwt.decode(token, options={"verify_signature": False})
    st.session_state["user"] = {
        "email": payload.get("sub"),
        "role": payload.get("role")
    }
    st.session_state["page"] = "home"

def auth_headers():
    return {
        "Authorization": f"Bearer {st.session_state['token']}"
    }

def logout():
    st.session_state.clear()
    st.rerun()
