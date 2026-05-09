
import streamlit as st


def boss_end_stage():
    st.title("💀 Defeat")

    st.error("You lost the boss fight. Try again!")

    if st.button("Try Again"):
        st.session_state.clear()
        st.session_state["stage"] = "setup"
        st.rerun()