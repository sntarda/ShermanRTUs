import streamlit as st
from scripts.auth import load_user_credentials, authenticate_user

def login():
    st.title("Login")

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    user_credentials = load_user_credentials('data/user_credentials.csv')

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password, user_credentials):
            st.session_state.authenticated = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

if 'authenticated' not in st.session_state or not st.session_state.authenticated:
    login()
else:
    st.sidebar.title("Main Menu")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()
