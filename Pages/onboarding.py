import streamlit as st

def onboarding():

    name = st.text_input("Enter you name")
    email = st.text_input("Enter Email")
    Gender = st.radio("Gender", ["Boy", "Girl"])
    age = st.slider("Enter Age")
    if st.form_submit_button("Submit"):
        st.session_state["needs_onboarding"] = False
        st.rerun