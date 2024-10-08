"""News articles for the Muir Woods case."""

import streamlit as st

st.header("Extra, Extra, Extra! Read all about it! 🗞")

with st.expander("### Internet Troll Takes Center Stage Amid Muir Woods Mystery"):
    with open("src/detective/docs/muir_woods/news/internet_troll.md", "r") as f:
        st.markdown(f.read())

with st.expander(
    "### Start-up Duo Raises $2M Pre-Seed for Revolutionary 'Cloud Farming'"
):
    with open("src/detective/docs/muir_woods/news/startup.md", "r") as f:
        st.markdown(f.read())

with st.expander(
    """### Florida Man Reflects on San Francisco Trip: "It’s Like the Ocean, But Fancier"""
):
    with open("src/detective/docs/muir_woods/news/florida.md", "r") as f:
        st.markdown(f.read())
