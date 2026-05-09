import streamlit as st


def end_stage():
    result = st.session_state.get("battle_result", "")

    if result == "win":
        st.title("🎉 Victory!")

        st.success("Congrats! You have beaten the boss!")

        st.write("""
The boss fades into glowing dust, but before everything becomes quiet,
you notice a strange symbol appear on the ground.

You realize this adventure is not over yet...
There is more to the story.
""")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Continue"):
                st.session_state["stage"] = "next_part"
                st.rerun()

        with col2:
            if st.button("End Game"):
                st.session_state.clear()
                st.success("Thanks for playing!")

    elif result == "lose":
        st.title("💀 Defeat")

        st.error("You lost the boss fight. Try again!")

        if st.button("Try Again"):
            st.session_state.clear()
            st.session_state["stage"] = "generate"
            st.rerun()