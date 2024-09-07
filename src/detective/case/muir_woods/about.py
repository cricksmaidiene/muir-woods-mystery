"""Landing page of mystery - for detectives"""

import streamlit as st
import os

st.title("Muir Woods Investigation 🏕")
st.caption("")

st.info(
    """
    A series of **seven** deaths have been discovered in and around the **Muir Woods, CA** area (pronounced 'me-er'). 
    The timeline of the deaths suggests a pattern.
    Initial investigations have raised more questions than answers, and it’s up to you to dig deeper
    """
)

time_of_year_panel, casualties_panel, timeline_panel = st.columns(3)

time_of_year_panel.metric("🍁 Time of Year", "Fall")
casualties_panel.metric("⚰️ Casualties", "Seven")
timeline_panel.metric("⏳ Timeline of Deaths", "2 weeks")

st.warning(
    "🌦 Rain and mist have complicated the investigation, obscuring potential evidence."
)

st.caption(
    """
    * You are now part of the task force assigned to investigate these deaths. 
    * Report to Detective Inspector Lestrade for further instructions.
    """
)

with st.expander("Fourth Wall"):
    st.caption(
        """
        #### General Information
        - All goals as well as story progression are self-contained in the application.
        - The mystery has two parts, with the second part unlocking after the first is solved.
        - The first involves investigating the muir woods deaths, and reporting the findings to the language model. It then unlocks Phase 2 to finish the story.

        #### Usage of Models and Data
        - This app sometimes uses a chat interface backed by an LLM to converse with the story's characters.
        - You need an `OPENAI_API_KEY`. More details in the **Application Keys** section below.        
        - The code for this application is open-sourced and does not store your key.
        - Chat data is not stored externally at any time, and is terminated once the session ends.
        """
    )

    st.caption(
        "The key will be used during your session as you use the chat interfaces."
    )
    openai_key_user_input: str = st.text_input(
        "Enter your OPENAI API KEY below", key="OPENAI_API_KEY"
    )
    if openai_key_user_input:

        os.environ["OPENAI_API_KEY"] = (
            st.secrets["GEN_USE_OPENAI_API_KEY"]
            if openai_key_user_input.lower() == st.secrets["OVERRIDE_PASSKEY"]
            else openai_key_user_input
        )

    st.caption(
        """
        If you do not possess a key, you may either:
        
        1. [Create an OpenAI key](https://platform.openai.com/api-keys) for self-use.
        2. [Reach out to me](https://twitter.com/Eash98) for an overriding passkey.
        """
    )
