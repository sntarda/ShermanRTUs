import streamlit as st
import pandas as pd

# Function to load user credentials from a CSV file
def load_user_credentials(file_path):
    return pd.read_csv(file_path)

# Function to authenticate user
def authenticate_user(username, password, user_credentials):
    user_row = user_credentials[(user_credentials['username'] == username) & (user_credentials['password'] == password)]
    return not user_row.empty

# Function to handle user login
def login():
    st.session_state.authenticated = False
    st.title("Login")

    user_credentials = load_user_credentials('data/user_credentials.csv')

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password, user_credentials):
            st.session_state.authenticated = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")
