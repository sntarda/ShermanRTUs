import streamlit as st
import pandas as pd

# Function to load user credentials from a CSV file
def load_user_credentials(file_path):
    return pd.read_csv(file_path)

# Function to authenticate user
def authenticate_user(username, password, user_credentials):
    user_row = user_credentials[(user_credentials['username'] == username) & (user_credentials['password'] == password)]
    return not user_row.empty

