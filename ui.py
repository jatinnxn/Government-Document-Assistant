import streamlit as st
from agent import generate_answer

st.set_page_config(page_title="US Gov Document Assistant", layout="wide")

st.title("US Government Document Assistant")
st.markdown("Ask any question based on government documents...")

user_query = st.text_input("Enter your question:")

if user_query:
    with st.spinner("Searching and generating answer..."):
        response = generate_answer(user_query)
        st.write(response)