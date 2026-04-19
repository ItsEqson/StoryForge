import streamlit as st
from ai import get_json_response
from Pages.prompts import CHAPTER_ONE_PROMPT, CHAPTER_TWO_PROMPT

def playing():

    
    if "turn_count" not in st.session_state:
        st.session_state["turn_count"] = 0

    if "current_chapter" not in st.session_state:
        st.session_state["current_chapter"] = []

    if "game_data" not in st.session_state:
        genre = st.session_state["genre"]
        gender = st.session_state["gender"]
        age = st.session_state["age"]
        learn = st.session_state["learn"]
        history = st.session_state["current_chapter"]
        turn = st.session_state["turn_count"]

        if turn == 0:
            system_prompt = CHAPTER_ONE_PROMPT
        else:
            system_prompt = CHAPTER_TWO_PROMPT

        user_prompt = f"""
The story genre should be {genre}.
The player is a {gender}.
The player is {age} years old.
The player wants to learn or improve at {learn}.

Previous story:
{history}

This is turn {turn + 1} of 3.
Make this a continuation of the last part of the story.

Return only valid JSON.
"""

        response = get_json_response(system_prompt, user_prompt)

        st.session_state["game_data"] = response

        st.session_state["current_chapter"] += "\n" + response.get("story", "")

    data = st.session_state["game_data"]

    st.header(data.get("story_title", f"Chapter {st.session_state['turn_count'] + 1}"))
    st.write(data.get("story", "No story generated."))

    st.subheader("📚 Lesson")
    st.write(data.get("lesson", "No lesson available."))

    st.subheader("🎯 Objective")
    st.write(data.get("objective", "No objective available."))

    st.subheader("⚔️ What do you do?")
    choices = data.get("choices", [])
    if choices:
        for i, choice in enumerate(choices):
            if st.button(choice, key=f"choice_{i}"):
                st.session_state["last_choice"] = choice
                st.success(f"You chose: {choice}")
                if st.session_state["turn_count"] < 2:
                    st.session_state["turn_count"] += 1

                    if "game_data" in st.session_state:
                        del st.session_state["game_data"]
    else:
        st.write("No choices available.")

    if st.session_state["turn_count"] < 2:
        st.session_state["turn_count"] += 1

        if "game_data" in st.session_state:
            del st.session_state["game_data"]
