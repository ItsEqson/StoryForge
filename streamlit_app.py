import streamlit as st
from Pages.boss_fight import boss_fight
from Pages.playing import playing
from Pages.generate import generate
from Pages.home import home
from Pages.onboarding import onboarding
from db import sign_up, sign_in, sign_out, get_profile
# from supabase import create_client, Client

st.image("StoryForgeLogo.png", width=200)

def initialize_state():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'current_user' not in st.session_state:
        st.session_state['current_user'] = None
    if 'user_db' not in st.session_state:
        st.session_state['user_db'] = {"Eqson": "SkinLake25"}
    if 'needs_onboarding' not in st.session_state:
        st.session_state["needs_onboarding"] = False
    if 'current_user_id' not in st.session_state:
        st.session_state['current_user_id'] = None
    if 'stage' not in st.session_state:
        st.session_state['stage'] = "None" # setup stage, playing stage, boss stages, end stage
    if 'turn_count' not in st.session_state:
        st.session_state['turn_count'] = 0
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'current_chapter' not in st.session_state:
        st.session_state['current_chapter'] = []
    if 'initial_story' not in st.session_state:
        st.session_state['initial_story'] = []
    if 'genre' not in st.session_state:
        st.session_state['genre'] = ""
    if 'gender' not in st.session_state:
        st.session_state['gender'] = ""
    if 'age' not in st.session_state:
        st.session_state['age'] = ""

initialize_state()

# @st.cache_resource
# def init_supabase() -> Client:
#     url = st.secrets["SUPABASE_URL"]
#     key = st.secrets["SUPABASE_KEY"]
#     return create_client(url, key)

# supabase = init_supabase()


def login():
    with st.form("login_form"):
        st.header("Log In")
        username = st.text_input("Enter Username")
        password = st.text_input("Enter Password", type = "password")

        if st.form_submit_button("Submit"):
            user, error = sign_in(username, password)
            if error:
                st.error("incorrect username or password")
            else:
                st.session_state['logged_in'] = True
                st.session_state['current_user'] = username
                st.session_state['current_user_id'] = user.id
                st.rerun()


def logout():
    st.session_state['logged_in'] = False
    st.session_state['current_user'] = None          

def signup():
    with st.form("sign_up"):
        st.header("Sign Up")
        username = st.text_input("Enter email")
        password = st.text_input("Enter Password", type = "password")

        if st.form_submit_button("Submit"):
            user, error = sign_up(username, password)
            if error:
                st.error(f"{error}")

            else:
                st.session_state['logged_in'] = True
                st.session_state["needs_onboarding"] = True
                st.session_state['current_user'] = username
                st.session_state['current_user_id'] = user.id
                st.rerun()



# if st.session_state['logged_in'] == False:
#     auth_screen()
# else:
#     home_sceen()
#     if st.button('Log Out'):
#         logout()
#         st.rerun()
#     # logged in (show home page or inside app)

# Navigation
if st.session_state['logged_in'] == False:
    st.title("Story Forge")

    tab1, tab2 = st.tabs( ["Login", "Sign Up"] )

    with tab1:
        login()
    with tab2:
        signup()

elif st.session_state["needs_onboarding"]:
    onboarding()
elif st.session_state['stage'] == "setup":
    generate()
elif st.session_state['stage'] == "playing":
    playing()
elif st.session_state['stage'] == "boss_fight":
    boss_fight()
elif st.session_state['stage'] == "end":
    pass
else:
    generate()


























