"""a list of dictionaries with victim names, locations of death, and lat/lng for Muir Woods locations"""

import pandas as pd
import numpy as np

victim_death_locations: list[dict] = [
    {
        "name": "Daniel McCluskey",
        "cause_of_death": "Fell near northern trailhead",
        "location": "Northern Trailhead, near the Dipsea Trail",
        "lat": 37.9095,
        "lng": -122.5770
    },
    {
        "name": "Sarah Bergenthal",
        "cause_of_death": "Drowned in a creek",
        "location": "Redwood Creek, near the Cathedral Grove",
        "lat": 37.8962,
        "lng": -122.5751
    },
    {
        "name": "Melanie Sanders",
        "cause_of_death": "Suspicious circumstances near overlook",
        "location": "Cardiac Hill Overlook, near the Ben Johnson Trail",
        "lat": 37.9098,
        "lng": -122.5807
    },
    {
        "name": "Tony Bergenthal",
        "cause_of_death": "Poisoned at a campsite",
        "location": "Lost Trail, near the Panoramic Highway",
        "lat": 37.8967,
        "lng": -122.5747
    },
    {
        "name": "Arthur Brane",
        "cause_of_death": "Violent encounter",
        "location": "Fern Creek Trail, near the intersection with the Lost Trail",
        "lat": 37.8956,
        "lng": -122.5715
    },
    {
        "name": "Marco \"Sid\" Sangrevo",
        "cause_of_death": "Violent encounter",
        "location": "Fern Creek Trail, near the intersection with the Lost Trail",
        "lat": 37.8956,
        "lng": -122.5715
    },
    {
        "name": "Tony Blake",
        "cause_of_death": "Stroke while hiking",
        "location": "Bootjack Campground, near the Bootjack Trail",
        "lat": 37.9008,
        "lng": -122.5798
        
    }
]


