import streamlit as st

with open("src/detective/docs/muir_woods/geography.md") as f:
    st.markdown(f.read())