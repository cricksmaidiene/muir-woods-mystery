import streamlit as st
from detective.config import PHASE_2_UNLOCKED


muir_woods_about = st.Page(
    "case/muir_woods/about.py",
    title="About",
    icon=":material/info:",
)
muir_woods_geography = st.Page(
    "case/muir_woods/geography.py",
    title="Geography",
    icon=":material/public:",
)
muir_woods_surroundings = st.Page(
    "case/muir_woods/surroundings.py",
    title="Surroundings",
    icon=":material/place:",
)
muir_woods_victim_profiles = st.Page(
    "case/muir_woods/victim_profiles.py",
    title="Victim Profiles",
    icon=":material/person_search:",
)
muir_woods_news = st.Page(
    "case/muir_woods/news.py",
    title="News",
    icon=":material/article:",
)


gambolini_family_profiles = st.Page(
    "case/gambolini_family/family_profiles.py",
    title="Gambolini Family Profiles",
    icon=":material/face:",
)

MUIR_WOODS_DIRECTORY: dict[str, list] = {
    "Muir Woods Mystery": [
        muir_woods_about,
        muir_woods_surroundings,
        muir_woods_geography,
        muir_woods_victim_profiles,
        muir_woods_news,
    ],
}
GAMBOLINI_DIRECTORY: dict[str, list] = {"Gambolini Family": [gambolini_family_profiles]}

pg = st.navigation({**MUIR_WOODS_DIRECTORY})

if PHASE_2_UNLOCKED:
    pg = st.navigation({**MUIR_WOODS_DIRECTORY, **GAMBOLINI_DIRECTORY})

pg.run()
