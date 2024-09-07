"""Victim Profile page for Muir Woods case."""

import streamlit as st
from detective.case.muir_woods.victims.daniel import get_daniel_data
from detective.case.muir_woods.victims.arthur import get_arthur_data
from detective.case.muir_woods.victims.marco import get_marco_data
from detective.case.muir_woods.victims.sarah import get_sarah_data
from detective.case.muir_woods.victims.tony_berg import get_tony_berg_data
from detective.case.muir_woods.victims.tony_blake import get_tony_blake_data
from detective.case.muir_woods.victims.melanie import get_melanie_data

victim_profile_map = {
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
