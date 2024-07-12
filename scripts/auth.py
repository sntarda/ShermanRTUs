import streamlit as st
import pandas as pd

def load_user_credentials(file_path):
    return pd.read_csv(file_path)

def authenticate_user(username, password, user_credentials):
    user_row = user_credentials[(user_credentials['username'] == username) & (user_credentials['password'] == password)]
    return not user_row.empty

def check_password(username, password):
    user_credentials = load_user_credentials('data/user_credentials.csv')
    return authenticate_user(username, password, user_credentials)
