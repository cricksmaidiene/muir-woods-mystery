"""Victim Profile page for Muir Woods case."""

import streamlit as st
from detective.data.muir_woods_geography.victims import victim_death_locations
from detective.case.muir_woods.victims.daniel import get_daniel_data
from detective.case.muir_woods.victims.arthur import get_arthur_data
from detective.case.muir_woods.victims.marco import get_marco_data
from detective.case.muir_woods.victims.sarah import get_sarah_data
from detective.case.muir_woods.victims.tony_berg import get_tony_berg_data
from detective.case.muir_woods.victims.tony_blake import get_tony_blake_data
from detective.case.muir_woods.victims.melanie import get_melanie_data

victim_names = [victim["name"] for victim in victim_death_locations]

victim_chosen = st.selectbox("Select Victim", ["", *victim_names])

if victim_chosen == "Daniel McCluskey":
    get_daniel_data()

elif victim_chosen == 'Marco "Sid" Sangrevo':
    get_marco_data()

elif victim_chosen == "Arthur Brane":
    get_arthur_data()

elif victim_chosen == "Sarah Bergenthal":
    get_sarah_data()

elif victim_chosen == "Tony Bergenthal":
    get_tony_berg_data()

elif victim_chosen == "Tony Blake":
    get_tony_blake_data()

elif victim_chosen == "Melanie Sanders":
    get_melanie_data()

elif victim_chosen == "":
    st.warning("Please select a victim to view their profile.")
