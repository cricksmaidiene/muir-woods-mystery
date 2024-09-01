import streamlit as st
from agents.lestrade.lestrade_chat import chat_with_lestrade

st.title("Muir Woods Investigation 🏕")

st.info("""
    A series of `seven` deaths have been discovered in and around the `Muir Woods, CA` area. 
    The timeline of the deaths suggests a pattern, though the exact connection between the victims remains unclear.
    """)

time_of_year_panel, casualties_panel, timeline_panel = st.columns(3)
time_of_year_panel.metric("🍁 Time of Year", "Fall")
casualties_panel.metric("⚰️ Casualties", "7")
timeline_panel.metric("⏳ Timeline of Deaths", "2 weeks")

st.warning("🌦 Rain and mist have complicated the investigation, obscuring potential evidence.")

with open("src/detective/docs/muir_woods/about.md") as f:
    st.markdown(f.read())

st.subheader("Speak with D.I Lestrade 🕵🏼‍♀️")
st.caption(
    """
    Lestrade's heading the investigation, and the task force reports to him. 
    You can ask him basic information about the case and he can point you in the right direction. 
    You'll need to ultimately submit evidence to him as well, to carry out further inquiries.
    """
)

chat_with_lestrade()
    