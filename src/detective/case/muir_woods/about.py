import streamlit as st

with open("src/detective/docs/muir_woods/about.md") as f:
    st.markdown(f.read())