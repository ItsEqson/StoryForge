import streamlit as st
from db import save_profile

def onboarding():
    with st.form("onboarding_form"):
        name = st.text_input("Enter your name")
        email = st.session_state['current_user']
        Gender = st.radio("Gender", ["Boy", "Girl"])
        age = st.slider("Enter Age")
        submitted = st.form_submit_button("Submit")
        if submitted:
            user_id = st.session_state.get("current_user_id")
            save_profile(user_id, {"name": name, "email": email})
            st.session_state["gender"] = Gender
            st.session_state["age"] = age
            st.session_state["needs_onboarding"] = False
            st.rerun()