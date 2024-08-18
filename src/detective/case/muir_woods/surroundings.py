"""A module to display the surrounding towns and estates of Muir Woods."""

import streamlit as st
import pydeck as pdk
import os
import json
import pandas as pd

from detective.data.muir_woods_geography.victim_sites import victim_death_locations


GEOGRAPHY_GEOJSON_PATH: str = "src/detective/data/muir_woods_geography"

muir_geography_geojson_files: list[str] = os.listdir(GEOGRAPHY_GEOJSON_PATH)

muir_geography_geojson_files = [
    f"{GEOGRAPHY_GEOJSON_PATH}/{x}"
    for x in muir_geography_geojson_files
    if x.endswith(".json")
]

pydeck_geojson_layers = []

for geojson_file in muir_geography_geojson_files:
    with open(geojson_file) as f:
        place_name: str = (
            geojson_file.split("/")[-1].replace("_", " ").split(".")[0].title()
        )
        geojson_data = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": json.load(f)["geojson"],
                    "properties": {"name": place_name},
                }
            ],
        }

    geojson_layer = pdk.Layer(
        "GeoJsonLayer",
        geojson_data,
        pickable=True,
        stroked=True,
        filled=True,
        extruded=False,
        get_fill_color=(
            [0, 0, 255, 50]
            if "muir woods" not in place_name.lower()
            else [255, 0, 0, 80]
        ),
        get_line_color=[0, 0, 0],
        get_line_width=50,
        coverage=1,
    )

    pydeck_geojson_layers.append(geojson_layer)


# Set the view state for the map (latitude, longitude, and zoom level)
view_state = pdk.ViewState(
    latitude=37.8999,
    longitude=-122.5194,
    zoom=10,
    bearing=0,
    pitch=0,
)

scatterplot_layer = pdk.Layer(
    "ScatterplotLayer",
    victim_death_locations,
    pickable=True,
    get_position=["lng", "lat"],
    get_radius=10,  # Adjust the radius of the points
    get_fill_color=[255, 0, 0, 200],  # Red color with some transparency
    get_line_color=[0, 0, 0],  # Outline color
    line_width_min_pixels=0.5,
)

# Create a Deck.gl map with the GeoJSON layer
r = pdk.Deck(
    layers=[pydeck_geojson_layers, scatterplot_layer],
    initial_view_state=view_state,
    tooltip={"text": "{name}"},
    map_style="mapbox://styles/mapbox/outdoors-v12",
)

# Main Call

st.markdown("# Muir Woods - Surrounding Towns and Estates")
st.markdown("> A map of the surrounding towns and estates of Muir Woods, with locations of victim deaths marked.")
st.pydeck_chart(r)

st.dataframe(pd.DataFrame(victim_death_locations))

with open("src/detective/docs/muir_woods/surroundings.md") as f:
    st.markdown(f.read())
