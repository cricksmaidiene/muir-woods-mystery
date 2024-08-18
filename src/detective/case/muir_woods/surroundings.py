"""A module to display the surrounding towns and estates of Muir Woods."""

import streamlit as st
import pydeck as pdk
import os
import json


GEOGRAPHY_GEOJSON_PATH: str = "src/detective/data/muir_woods_geography"

muir_geography_geojson_files: list[str] = os.listdir(GEOGRAPHY_GEOJSON_PATH)

muir_geography_geojson_files = [
    f"{GEOGRAPHY_GEOJSON_PATH}/{x}" for x in muir_geography_geojson_files
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
            [0, 0, 255, 50] if "muir woods" not in place_name.lower() else [255, 0, 0, 80]
        ),
        get_line_color=[0, 0, 0],
        get_line_width=100,
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

# Create a Deck.gl map with the GeoJSON layer
r = pdk.Deck(
    layers=pydeck_geojson_layers,
    initial_view_state=view_state,
    tooltip={"text": "{name}"},
    map_style="mapbox://styles/mapbox/outdoors-v12",
)

# Main Call

st.markdown("# Muir Woods - Surrounding Towns and Estates")
st.pydeck_chart(r)

with open("src/detective/docs/muir_woods/surroundings.md") as f:
    st.markdown(f.read())