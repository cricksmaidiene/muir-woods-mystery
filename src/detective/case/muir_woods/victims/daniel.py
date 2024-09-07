"""Daniel McCluskey's victim profile data"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


def get_daniel_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "57")
    time_of_death.metric("Time of Death", "7.31 PM")
    origin_location.metric("Origin", "Mill Valley, CA")

    st.error("Fell near northern trailhead")

    st.json(
        {
            "Occupation": "Retired Electrical Engineer",
            "Marital Status": "Divorced",
            "Children": "None",
            "Last Known Whereabouts": "Northern trailhead, Muir Woods",
        }
    )

    with st.expander("### Background"):
        st.caption(
            """
        - **Occupation:** Daniel McCluskey was a retired electrical engineer who had spent 35 years working for a major utility company in the Bay Area. Known for his meticulous nature and attention to detail, Daniel was highly respected in his field. Since retirement, he became an avid hiker and frequently visited Muir Woods for solitary treks.
  
        - **Personality:** Daniel was known to be a quiet, introspective man with few close relationships. He enjoyed the solitude of nature and often spent days hiking alone. His neighbors described him as a "loner," but one who was always friendly and polite in brief interactions.

        - **Hobbies:** Besides hiking, Daniel had a keen interest in amateur radio and occasionally volunteered at a local wildlife preservation society. However, he kept a low profile and was not deeply involved in community activities.

        - **Divorce:** Daniel had gone through a bitter divorce five years prior. His ex-wife, `Linda McCluskey-Taylor`, had moved out of state and had not been in contact with him for over three years. There was no known ongoing legal or personal conflict between them.

        - **Financial Status:** Daniel was financially stable, living off his pension and savings. There were no significant debts or recent large transactions that raised suspicion.
        
        - **Social Connections:** He had a distant relationship with his neighbors and was rarely seen with company. Daniel had no known enemies, though a former colleague had once mentioned a mild workplace disagreement from years ago, which was never considered serious.
        
        - **Incident History:** Known for occasional trespassing into the **Bellingham Estate** adjacent to Muir Woods during hikes; warned multiple times but no legal action taken.
        """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error(
            "Initially determined to be blunt force trauma to the head, most probably consistent with a fall from a height."
        )

        st.caption("### Details on Time of Death")
        st.caption(
            """
            Medically it's supposed to be midnight, but we estimate around twilight because 
            Daniel would have made his way back home before nightfall and his smartwatch appears 
            to have zero heart rate since. The mist and surrounding environment muddle the actual time of death, 
            and the body was discovered the following morning.
        """
        )

    with st.expander("### Whereabouts & Witness Statements"):
        st.info("Last seen at  `2.30PM`  near the northern trailhead")
        st.caption(
            """
            - **Witness Statement:** 
                - A fellow hiker reported seeing Daniel at around `2:30 PM` near the northern trailhead. 
                - He was heading deeper into the woods and appeared to be in good spirits. 
                - The witness also noted that Daniel seemed to be carrying a small, uncharacteristic package, perhaps a thermos or similar item. This was not found at the scene.
            - **Route:** He was known to take a specific trail that led to a secluded overlook, where he often spent time reflecting and taking in the scenery.
        """
        )

    with st.expander("### Evidence"):
        st.caption(
            """
            - **Mobile Phone Data:** Due to poor reception in the area, Daniel's phone records are inconclusive. His phone was last active before he entered the woods, and there was no signal for the rest of the day.
            - **Radio Logs**: Daniel was in contact with various radio frequencies in the days leading up to his disappearance. 
            - **Surveillance Footage:** Limited camera coverage in the area did not capture Daniel after entering Muir Woods.
            - **Smartwatch Data:** Daniel's smartwatch recorded his heart rate throughout the day. 
            - **Thermos:** A thermos flask, most likely belonging to Daniel was found some 800 yards from the body. It appeared discarded. Samples from the thermos are being analyzed.
        """
        )

        st.caption("### Additional Notes")
        st.caption(
            """
            - Small abrasions found on his hands and knees, consistent with attempts to break his fall.
            - No significant signs of a struggle were noted at the scene.
            - Soil samples near the body indicated slight disturbances in the ground and nearby plants. 
            Likely the victim trying to cling onto something before falling.
        """
        )

    with st.expander("### Daniel's Radio Logs"):
        st.caption(
            "Daniel used a short-wave radio to communicate with other enthusiasts. The radio logs are based on receiving stations' records. Radios are especially useful in areas with poor cell reception. Double click a message to read more."
        )
        # Creating a dataframe from the provided markdown data
        radio_logs = pd.DataFrame(
            {
                "Time of Log": [
                    "7 days ago",
                    "6 days ago",
                    "5 days ago",
                    "4 days ago",
                    "4 days ago",
                    "3 days ago",
                    "2 days ago",
                    "1 day ago",
                    "Day of Death",
                    "Time of Death",
                ],
                "Signal Strength": [
                    3,
                    1,
                    4,
                    4,
                    5,
                    4,
                    3,
                    4,
                    5,
                    5,
                ],
                "Frequency": [
                    "145.320 MHz",
                    "145.320 MHz",
                    "146.580 MHz",
                    "144.200 MHz",
                    "147.000 MHz",
                    "145.800 MHz",
                    "146.940 MHz",
                    "144.400 MHz",
                    "146.520 MHz",
                    "All frequencies",
                ],
                "Conversation Summary": [
                    "Brief chat with a fellow radio enthusiast about upcoming weather patterns in the Bay Area.",
                    "Radio static sounds for brief seconds, poor connection",
                    "Conversation with a friend about their favorite hiking trails in Muir Woods.",
                    "Solo transmission detailing his planned hiking route in Muir Woods: starting at the northern trailhead, looping through a secluded overlook and ending by the creek.",
                    "Radio static sounds for multiple minutes, connection live but no conversation heard",
                    "Discussion with a hiking group about gear maintenance and survival tips.",
                    "Brief transmission about a recent hike, mentioning how peaceful the trails were that day.",
                    "Casual conversation with a local contact about upcoming amateur radio events.",
                    "Detailed projected trail he was going to take for the day, mentioning all the pitsops and trails.",
                    "Radio static sounds, open for about a minute. connection live, but no conversation heard. At the end of the minute, a signal was recorded before losing connection.",
                ],
            }
        )

        st.dataframe(
            radio_logs,
            column_config={
                "Signal Strength": st.column_config.ProgressColumn(
                    "Signal Strenth",
                    width="small",
                    min_value=0,
                    max_value=5,
                    format="%d",
                ),
                "Conversation Summary": st.column_config.TextColumn(
                    "Conversation Summary", width="large"
                ),
            },
            hide_index=True,
        )

        st.caption("Final signal from radio logs before losing connection:")
        st.audio(
            "https://cdn.pixabay.com/download/audio/2023/01/29/audio_1b1bbc3316.mp3?filename=sos-signal-137144.mp3",
            loop=True,
        )

    with st.expander("### Daniel's Heart Rate"):
        st.warning(
            "The initial heart rates are consistent with heavy exercise, followed by a sudden spike which could is consistent with shock and rise in adrenaline."
        )

        @st.cache_data
        def get_daniel_heart_rate() -> pd.DataFrame:
            # Create a date range from 7:15 PM to 7:30 PM at 1-minute intervals
            time_index = pd.date_range(
                start="2024-08-18 19:15", end="2024-08-18 19:30", freq="T"
            )

            # Simulate heart rates for general exercise (normal range for a 57-year-old might be 90-120 bpm)
            heart_rates = np.random.randint(90, 120, size=len(time_index))

            # Add a spike in heart rate due to a fight at 7:30 PM for about 15-20 seconds
            fight_duration = pd.date_range(
                start="2024-08-18 19:30:00", end="2024-08-18 19:30:20", freq="S"
            )
            fight_heart_rates = np.random.randint(140, 160, size=len(fight_duration))

            # Add a blank (0 bpm) after 7:31 PM
            blank_time = pd.date_range(
                start="2024-08-18 19:31", end="2024-08-18 19:31", freq="T"
            )
            blank_heart_rate = [0]

            # Combine the data
            time_index = time_index.append(fight_duration).append(blank_time)
            heart_rates = np.concatenate(
                [heart_rates, fight_heart_rates, blank_heart_rate]
            )

            # Create the DataFrame
            daniel_heart_rate_df = pd.DataFrame(
                {"Time": time_index, "Heart Rate (bpm)": heart_rates}
            )
            return daniel_heart_rate_df

        st.write(
            px.line(
                get_daniel_heart_rate(),
                x="Time",
                y="Heart Rate (bpm)",
                markers=True,
                title="Daniel McCluskey's Heart Rate Until his Death (Smartwatch Data)",
            )
        )
