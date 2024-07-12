import streamlit as st
from scripts.auth import check_password

def login():
    st.title('Login')
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if check_password(username, password):
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    st.success("Logged in")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({'logged_in': False}))
