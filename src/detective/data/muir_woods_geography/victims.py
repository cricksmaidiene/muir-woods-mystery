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


def get_daniel_heart_rate() -> pd.DataFrame:
    # Create a date range from 7:15 PM to 7:30 PM at 1-minute intervals
    time_index = pd.date_range(start="2024-08-18 19:15", end="2024-08-18 19:30", freq="T")

    # Simulate heart rates for general exercise (normal range for a 57-year-old might be 90-120 bpm)
    heart_rates = np.random.randint(90, 120, size=len(time_index))

    # Add a spike in heart rate due to a fight at 7:30 PM for about 15-20 seconds
    fight_duration = pd.date_range(start="2024-08-18 19:30:00", end="2024-08-18 19:30:20", freq="S")
    fight_heart_rates = np.random.randint(140, 160, size=len(fight_duration))

    # Add a blank (0 bpm) after 7:31 PM
    blank_time = pd.date_range(start="2024-08-18 19:31", end="2024-08-18 19:31", freq="T")
    blank_heart_rate = [0]

    # Combine the data
    time_index = time_index.append(fight_duration).append(blank_time)
    heart_rates = np.concatenate([heart_rates, fight_heart_rates, blank_heart_rate])

    # Create the DataFrame
    daniel_heart_rate_df = pd.DataFrame({"Time": time_index, "Heart Rate (bpm)": heart_rates})
    return daniel_heart_rate_df

