from Pages.prompts import CHAPTER_ONE_PROMPT, CHAPTER_TWO_PROMPT, CHAPTER_THREE_PROMPT, BOSS_FIGHT_PROMPT
import streamlit as st
from ai import get_json_response

import random
import streamlit as st
from ai import get_json_response


def generate_boss_turn():
    genre = st.session_state.get("genre", "fantasy")
    learn = st.session_state.get("learn", "problem solving")
    difficulty = st.session_state.get("difficulty", "Medium")
    story_history = st.session_state.get("current_chapter", "")
    boss_hp = st.session_state.get("boss_hp", "unknown")
    player_hp = st.session_state.get("player_hp", "unknown")
    turn = st.session_state.get("boss_turn", 1)

    user_prompt = f"""
The story genre is {genre}.
The player wants to learn or improve at {learn}.
The difficulty is {difficulty}.

Previous story:
{story_history}

Boss turn: {turn}
Current player HP: {player_hp}
Current boss HP: {boss_hp}

Create a new boss fight turn.
The choices must be different from the last turn.
The correct choice must appear in a different slot if possible.

Return only valid JSON.
"""

    data = get_json_response(BOSS_FIGHT_PROMPT, user_prompt)

    choices = data.get("choices", [])
    correct_choice = data.get("correct_choice", "")

    if correct_choice in choices:
        random.shuffle(choices)
        data["choices"] = choices

    return data


def boss_fight():
    st.title("🐉 Boss Fight")

    if "boss_turn" not in st.session_state:
        st.session_state["boss_turn"] = 1

    if "boss_data" not in st.session_state:
        data = generate_boss_turn()

        st.session_state["boss_data"] = data
        st.session_state["player_hp"] = data.get("player_hp", 100)
        st.session_state["boss_hp"] = data.get("boss_hp", 100)

    data = st.session_state["boss_data"]

    st.header(data.get("boss_name", "Final Boss"))
    st.write(data.get("story", "The boss appears!"))

    st.subheader("⚡ Boss Ability")
    st.write(data.get("boss_ability", "Unknown ability"))

    st.subheader("❤️ Health")
    st.write(f"Player HP: {st.session_state['player_hp']}")
    st.write(f"Boss HP: {st.session_state['boss_hp']}")

    st.subheader("📚 Lesson")
    st.write(data.get("lesson", "No lesson available."))

    st.subheader("🎯 Objective")
    st.write(data.get("objective", "Defeat the boss."))

    st.subheader("⚔️ Choose Your Action")

    choices = data.get("choices", [])
    correct_choice = data.get("correct_choice", "")

    for i, choice in enumerate(choices):
        if st.button(choice, key=f"boss_choice_{st.session_state['boss_turn']}_{i}"):

            outcomes = data.get("outcomes", {})

            if choice == correct_choice:
                st.success(outcomes.get("correct_choice", "Correct! The boss loses HP."))
                st.session_state["boss_hp"] -= 20
            else:
                st.error(outcomes.get("wrong_choice", "Wrong! You lose HP."))
                st.session_state["player_hp"] -= 20

            if st.session_state["boss_hp"] <= 0:
                st.success("🎉 You defeated the boss!")
                st.balloons()

            elif st.session_state["player_hp"] <= 0:
                st.error("💀 You lost the boss fight. Try again!")

            else:
                st.session_state["boss_turn"] += 1
                del st.session_state["boss_data"]
                st.rerun()