"""A chat interface with Detective Inspector Lestrade."""

import streamlit as st
from agents.lestrade import chat_with_lestrade  # type: ignore

st.subheader("Speak with D.I Lestrade 🕵🏼‍♀️")

st.caption(
    """
    Lestrade's heading the investigation, and the task force reports to him. 
    You can ask him basic information about the case and he can point you in the right direction. 
    You'll need to ultimately submit evidence to him as well, to carry out further inquiries.
    """
)

with st.expander("About Lestrade"):
    st.caption(
        """
        - Seasoned investigator (over 25 y/o exp) with a keen eye for detail.
        - Husband to Cassandra and father to Rachel.
        - Of Irish descent, and enjoys lake fishing
        - Strong connections to the force and fire department.
        - Press and stakeholders are behind him to solve the case.

        😶‍🌫️ Lestrade does not have conversation history, and will treat each prompt independently.
        """
    )

chat_with_lestrade()
