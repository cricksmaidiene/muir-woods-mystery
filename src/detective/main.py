import streamlit as st


muir_woods_about = st.Page(
    "case/muir_woods/about.py",
    title="About",
    icon=":material/info:",
)
muir_woods_lestrade = st.Page(
    "case/muir_woods/lestrade.py",
    title="D.I Lestrade",
    icon=":material/chat_bubble_outline:",
)
muir_woods_geography = st.Page(
    "case/muir_woods/geography.py",
    title="Geography",
    icon=":material/public:",
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
muir_woods_submission = st.Page(
    "case/muir_woods/submit_findings.py",
    title="Submit Findings",
    icon=":material/assignment_turned_in:",
)


MUIR_WOODS_DIRECTORY: dict[str, list] = {
    "Muir Woods Mystery": [
        muir_woods_about,
        muir_woods_lestrade,
        muir_woods_geography,
        muir_woods_victim_profiles,
        muir_woods_news,
        muir_woods_submission,
    ],
}

pg = st.navigation({**MUIR_WOODS_DIRECTORY})

pg.run()
