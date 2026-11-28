import streamlit as st

st.title("Welcome to My Page of PDF")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("Your PDF Uploaded Successfully")
