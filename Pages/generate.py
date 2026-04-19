import streamlit as st

def generate():
    st.title("Story Generator")

    genre = st.text_input("What genre do you want the story to be about?")
    learn = st.text_input("What topic would you like to learn or get better at?")

    if st.button("Submit", key="generate_button"):
        st.session_state["genre"] = genre
        st.session_state["learn"] = learn

        # reset game
        st.session_state["turn_count"] = 0
        st.session_state["current_chapter"] = ""

        st.session_state['stage'] = "playing"

