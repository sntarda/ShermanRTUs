import streamlit as st
from login import login

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    login()
else:
    st.sidebar.title("Main Menu")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({'logged_in': False}))
    st.sidebar.write("---")
    st.sidebar.write("**Buildings**")
    if st.sidebar.button("Building 1001"):
        st.experimental_rerun()
    if st.sidebar.button("Building 1055"):
        st.experimental_rerun()
    if st.sidebar.button("Building 1057"):
        st.experimental_rerun()
    if st.sidebar.button("Building 1059"):
        st.experimental_rerun()

    st.title('Dashboard')
    st.write('Company Information:')
    st.write('Company Name: Example Company')
    st.write('Address: 123 Example St, City, Country')
    st.write('Phone: (123) 456-7890')
