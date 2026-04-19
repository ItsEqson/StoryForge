import streamlit as st

def onboarding():
    with st.form("onboarding_form"):
        name = st.text_input("Enter your name")
        email = st.text_input("Enter Email")
        Gender = st.radio("Gender", ["Boy", "Girl"])
        age = st.slider("Enter Age")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state["needs_onboarding"] = False
            st.rerun()