"""Melanie Sanders' victim profile data"""

import streamlit as st


def get_melanie_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "41")
    time_of_death.metric("Time of Death", "5.45 PM")
    origin_location.metric("Origin", "Corte Madera, CA")

    st.caption("Cause of Death")
    st.error("Shot dead in the head. Likely committed suicide")

    st.json(
        {
            "Occupation": "Environmental Consultant",
            "Marital Status": "Single",
            "Children": None,
            "Last Known Whereabouts": None,
        }
    )

    with st.expander("### Background"):
        st.caption(
            """
        - **Occupation:** Melanie Sanders worked as an environmental consultant. Her work often took her to remote locations, where she conducted assessments and provided guidance on reducing environmental impact.

        - **Personality:** Melanie was a strong-willed and independent woman. She was confident in her abilities and wasn’t afraid to speak her mind, whether in a professional setting or in her personal life.

        - **Relationships:** Melanie was close to a small circle of friends, but she kept her personal life private. She was single and had no immediate family in the area. Those who knew her described her as fiercely independent, with a strong sense of purpose and direction in life. She was raised by a single mother who passed away due to natural causes just as she was getting started with her career. It left a huge blow on her, also leaving her consultancy in need of financial backing, and making her more responsible to herself.
        """
        )

    with st.expander("### Witness Statements & Last Known Whereabouts"):
        st.caption(
            """
            - **Friend's Statement:** A close friend of Melanie’s provided the following statement:
            
                - “Melanie was always so sure of herself. She knew what she wanted in life and went after it without hesitation. She was in a really good place, both personally and professionally, so the news of her death just doesn’t make sense. She wasn’t the type to take risks on the trail—she knew what she was doing out there. It feels like there’s something we’re missing.”       
            """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error(
            "Melanie Sanders was found shot dead in the head. The bullet wound was consistent with an unmarked high-caliber pistol, found in her arms. The angle of entry and exit suggests that the shot was self-inflicted."
        )

        st.caption("### Details on Time of Death")
        st.caption(
            """
            Melanie's body was found at the base of a steep incline near a remote overlook in Muir Woods. She was shot dead in the head, with the bullet entering from the right temple and exiting through the left side of her head.
        """
        )

    with st.expander("### Melanie's Financial Backers"):
        backer_data = [
            {
                "Backer Name": "GreenEarth Initiative",
                "Type": "Non-Profit",
                "Investment Level": 10000,
                "LP Count": 5,
            },
            {
                "Backer Name": "Eco-Futures Foundation",
                "Type": "Non-Profit",
                "Investment Level": 45000,
                "LP Count": 7,
            },
            {
                "Backer Name": "Bay Area Sustainability Fund",
                "Type": "Private Trust",
                "Investment Level": 18000,
                "LP Count": 4,
            },
            {
                "Backer Name": "Clean Waters Project",
                "Type": "Corporate Sponsor",
                "Investment Level": 25000,
                "LP Count": 3,
            },
            {
                "Backer Name": "Northern California Environmental Fund",
                "Type": "Non-Profit",
                "Investment Level": 30000,
                "LP Count": 6,
            },
            {
                "Backer Name": "Sustainable Solutions Group",
                "Type": "Corporate Sponsor",
                "Investment Level": 20000,
                "LP Count": 4,
            },
            {
                "Backer Name": "Earth Guardians Initiative",
                "Type": "Non-Profit",
                "Investment Level": 15000,
                "LP Count": 2,
            },
            {
                "Backer Name": "Sierra Green Ventures",
                "Type": "Venture Capital",
                "Investment Level": 415000,
                "LP Count": 1,
            },
            {
                "Backer Name": "Pacific Environmental Defense Fund",
                "Type": "Non-Profit",
                "Investment Level": 50000,
                "LP Count": 8,
            },
            {
                "Backer Name": "Coastal Conservation Coalition",
                "Type": "Non-Profit",
                "Investment Level": 40000,
                "LP Count": 6,
            },
            {
                "Backer Name": "Future Generations Initiative",
                "Type": "Private Investor",
                "Investment Level": 100000,
                "LP Count": 5,
            },
        ]

        st.dataframe(backer_data, hide_index=True)
