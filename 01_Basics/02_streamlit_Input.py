import streamlit as st

st.title("Welcome to My page by Atharv T. Bhosale")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome")
