"""Victim Profile page for Muir Woods case."""

import streamlit as st
from detective.case.muir_woods.victims.daniel import get_daniel_data
from detective.case.muir_woods.victims.arthur import get_arthur_data
from detective.case.muir_woods.victims.marco import get_marco_data
from detective.case.muir_woods.victims.sarah import get_sarah_data
from detective.case.muir_woods.victims.tony_berg import get_tony_berg_data
from detective.case.muir_woods.victims.tony_blake import get_tony_blake_data
from detective.case.muir_woods.victims.melanie import get_melanie_data


def profile_home():
    st.subheader("Victim Profiles")
    st.warning("Select a victim to view their profile")

    st.markdown(
        """
        General instructions when examining victim profiles:

        - `Time of Death` is always made by the coroner, and is an estimation based on biological evidence and Muir Woods weather conditions. No time of death is precise down to the exact minute / second as listed.
        - `Cause of Death` is the preliminary finding by the coroner. Further investigation may reveal more details. 
        - You may ask questions to Lestrade 🕵🏼‍♂️ about specific details / evidence. He may answer some, and for others he will redirect you to the case files. Examples:
            
            - "What do you make of **Sarah's** social media posts?"
            - "Do you think foul play is involved in **Tony Berg's** death?"        
        """
    )


victim_profile_map = {
    "Home": profile_home,
    "1. Daniel McCluskey": get_daniel_data,
    "2. Sarah Bergenthal": get_sarah_data,
    "3. Melanie Sanders": get_melanie_data,
    "4. Tony Bergenthal": get_tony_berg_data,
    "5. Tony Blake": get_tony_blake_data,
    "6. Arthur Brane": get_arthur_data,
    '7. Marco "Sid" Sangrevo': get_marco_data,
}

victim_chosen = st.selectbox("Select Victim", victim_profile_map.keys())

victim_profile_map.get(victim_chosen, lambda: None)()
