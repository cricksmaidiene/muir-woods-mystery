import streamlit as st

with open("src/detective/docs/muir_woods/about.md") as f:
    st.markdown(f.read())

st.error("Are these accidental deaths or a homicide? If so, who is the perpetrator?")
st.warning("What is our biggest lead and why? Given the evidence, where can we continue our line of inquiry?")