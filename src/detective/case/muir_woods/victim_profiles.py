import streamlit as st
from detective.data.muir_woods_geography.victims import (
    victim_death_locations,
    get_daniel_heart_rate,
)
import plotly.express as px
import pandas as pd

victim_names = [victim["name"] for victim in victim_death_locations]

victim_chosen = st.selectbox("Select Victim", ["", *victim_names])

if victim_chosen == "Daniel McCluskey":
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "57")
    col2.metric("Time of Death", "7.31 PM")
    col3.metric("Origin", "Mill Valley, CA")

    with open("src/detective/docs/muir_woods/daniel.md", "r") as f:
        st.markdown(f.read())

    daniel_heart_rate_df: pd.DataFrame = get_daniel_heart_rate()
    st.write(
        px.line(
            daniel_heart_rate_df,
            x="Time",
            y="Heart Rate (bpm)",
            markers=True,
            title="Daniel McCluskey's Heart Rate Until his Death (Smartwatch Data)",
        )
    )

elif victim_chosen == 'Marco "Sid" Sangrevo':
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "39")
    col2.metric("Time of Death", "6.25 PM")
    col3.metric("Origin", "Columbus, OH")
    with open("src/detective/docs/muir_woods/marco.md", "r") as f:
        st.markdown(f.read())

elif victim_chosen == "Arthur Brane":
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "32")
    col2.metric("Time of Death", "6.23 PM")
    col3.metric("Origin", "San Francisco, CA")
    with open("src/detective/docs/muir_woods/arthur.md", "r") as f:
        st.markdown(f.read())

elif victim_chosen == "Sarah Bergenthal":
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "27")
    col2.metric("Time of Death", "4.47 PM")
    col3.metric("Origin", "Sausalito, CA")
    with open("src/detective/docs/muir_woods/sarah.md", "r") as f:
        st.markdown(f.read())

elif victim_chosen == "Tony Bergenthal":
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "29")
    col2.metric("Time of Death", "9.31 PM")
    col3.metric("Origin", "Sausalito, CA")
    with open("src/detective/docs/muir_woods/tony_bergenthal.md", "r") as f:
        st.markdown(f.read())

elif victim_chosen == "Tony Blake":
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "58")
    col2.metric("Time of Death", "10.15 AM")
    col3.metric("Origin", "Larkspur, CA")
    with open("src/detective/docs/muir_woods/tony_blake.md", "r") as f:
        st.markdown(f.read())

elif victim_chosen == "Melanie Sanders":
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", "41")
    col2.metric("Time of Death", "5.45 PM")
    col3.metric("Origin", "Corte Madera, CA")
    with open("src/detective/docs/muir_woods/melanie.md", "r") as f:
        st.markdown(f.read())
