import streamlit as st
from Pages.generate import generate

def home():
    st.header("StoryForge App 🚀")
    st.write("Your adventure begins here!")

    if st.button("Start"):
        st.session_state['stage'] = "setup"
        st.rerun()