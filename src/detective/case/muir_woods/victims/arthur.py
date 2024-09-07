"""Arthur Brane's victim profile data"""

import streamlit as st


def get_arthur_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "32")
    time_of_death.metric("Time of Death", "6.23 PM")
    origin_location.metric("Origin", "San Francisco, CA")

    st.error("Asphyxiation, likely due to strangulation")

    st.json(
        {
            "Occupation": "Financial Analyst",
            "Marital Status": "Married to Emily Brane.",
            "Children": "None",
            "Last Known Whereabouts": "CCTV Footage walking into the woods with Marco Sangrevo",
        }
    )

    with st.expander("### Background"):
        st.caption(
            """
        - **Personality:** Arthur was a confident and sociable man, well-liked by his colleagues and known for his ability to connect with others.

        - **Family**: Arthur was married to Emily Brane, a relationship that had been a constant in his life since college. They had no children. Arthur was raised by Foster parents.

        - **Recent Behavior:** Over the past week, Arthur had become increasingly troubled. His wife, Emily, noted that he had been spending more time alone, often anxious in thought, and seemed preoccupied with something he wouldn’t discuss. Despite her attempts to reach out to him, Arthur remained distant, leaving her concerned but unaware of the true nature of his worries.
        """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error(
            "Asphyxiation, likely due to strangulation. High tracheal bruising."
        )

        st.caption("### Details on Time of Death")
        st.caption(
            """
            The body was found in a state of rigor mortis, indicating the victim had been deceased for several hours.
            Lividity was present on the back and posterior of the body, consistent with the position in which the body was found.
            No signs of toxic substances were found in the victim
        """
        )

    with st.expander("### Whereabouts & Witness Statements"):
        st.info("Last seen with Marco Sangrevo")
        st.caption(
            """
            - **Final Meeting:** Arthur was captured on CCTV footage meeting Marco "Sid" Sangrevo in a public location. The footage shows them speaking briefly before walking into the woods together. The nature of their conversation and why they were meeting remains unclear.
            - **Discovery:** Arthur’s body was found asphyxiated near Sid’s at the edge of Muir Woods. The grass around Arthur was highly disturbed indicating he was trying to fight off being asphyxiated. The ground around Sid was not disturbed, and there were a third pair of footprints identified near the bodies, which is believed to be the one who probably shot Sid.

            - Emily Brane provided the following statement:

            ```markdown
            Arthur and I have been together since college. 
            He was always the smartest person in the room, the one everyone 
            relied on for advice. 
            We built a good life together—Arthur worked so hard to provide for us, 
            and I always admired his dedication. 
            He was devoted to his work as a financial analyst, and though it 
            kept him busy, 
            he always made time for us. We were both so grateful 
            when he received that scholarship for college. 
            He wouldn’t have been able to afford it otherwise. 

            The Gambolinis funded his education, and it’s something 
            we’ve always appreciated. They were incredibly generous, especially 
            to someone like Arthur, who had no family to support him through school. 
            He worked tirelessly to prove that their investment in him was worth it.
            When Mr. Gambolini passed, we mourned with everyone else. 

            We’ve had our share of struggles, like any couple, but we’ve always 
            come through stronger. 
            That’s why it’s been so hard to see him like this lately.
            Over the past week, he seemed different—distant, distracted. 
            I could tell something was weighing on him, but every time I asked, 
            he would just say it was work stress.

            But I never imagined it would lead to something like this. 
            He never kept secrets from me, at least none that I knew of…
            ```
        """
        )

    with st.expander("### Evidence"):
        st.caption(
            """
            - **Clothing:** 
                - At the time of his death, Arthur was dressed in business-casual attire. 
                - His shoes and clothing bore signs of dirt and foliage from the woods, suggesting he had been walking through the area before his death.
                - He had on all apparels like his Watch, wallet and phone, but his phone was found switched off. 

            - **Note to Wife:** Before leaving to meet Sid, Arthur left a cryptic note for Emily. It read:

                ```
                “Emily, there are things I need to face—things I should have told you long ago. 
                Things that has been a part of me since I was born, wherever that was.

                I’ve been wrestling with this for years, and now I fear it’s too late to make things right. 

                Whatever happens, know that I love you, and I’m sorry for the burden I’ve carried alone. —Art"
                ```
        """
        )

    with st.expander("### Arthur's Call Log"):

        call_log = [
            {
                "Time of Call": "08:30 AM",
                "Caller ID": "E. Brane (Wife)",
                "Phone Number": "(415) 555-1234",
                "Duration": "12 min",
                "Call Type": "Incoming",
            },
            {
                "Time of Call": "10:45 AM",
                "Caller ID": "A. Secura (Office)",
                "Phone Number": "(415) 555-8765",
                "Duration": "3 min",
                "Call Type": "Outgoing",
            },
            {
                "Time of Call": "10:50 AM",
                "Caller ID": "B. Fett (Friend)",
                "Phone Number": "(415) 555-8765",
                "Duration": "Missed Call",
                "Call Type": "Incoming",
            },
            {
                "Time of Call": "12:15 PM",
                "Caller ID": "D. Smith (Unknown)",
                "Phone Number": "(415) 555-5678",
                "Duration": "5 min",
                "Call Type": "Incoming",
            },
            {
                "Time of Call": "02:30 PM",
                "Caller ID": "B. Huxley (Office)",
                "Phone Number": "(415) 555-4321",
                "Duration": "8 min",
                "Call Type": "Outgoing",
            },
            {
                "Time of Call": "04:30 PM",
                "Caller ID": "M. Sanders (Unknown)",
                "Phone Number": "(415) 555-7890",
                "Duration": "Missed Call",
                "Call Type": "Outgoing",
            },
            {
                "Time of Call": "09:00 AM",
                "Caller ID": "E. Brane (Wife)",
                "Phone Number": "(415) 555-1234",
                "Duration": "6 min",
                "Call Type": "Outgoing",
            },
            {
                "Time of Call": "10:00 AM",
                "Caller ID": "J. Yang (Office)",
                "Phone Number": "(415) 555-5678",
                "Duration": "7 min",
                "Call Type": "Incoming",
            },
            {
                "Time of Call": "03:45 PM",
                "Caller ID": "Unknown Number",
                "Phone Number": "Unknown",
                "Duration": "10 seconds",
                "Call Type": "Incoming",
            },
            {
                "Time of Call": "06:10 PM",
                "Caller ID": "E. Winters (Friend)",
                "Phone Number": "(415) 555-8765",
                "Duration": "Missed Call",
                "Call Type": "Incoming",
            },
            {
                "Time of Call": "06:15 PM",
                "Caller ID": "E. Winters (Friend)",
                "Phone Number": "(415) 555-8765",
                "Duration": "15 min",
                "Call Type": "Outgoing",
            },
            {
                "Time of Call": "09:30 AM",
                "Caller ID": "Unknown Number",
                "Phone Number": "Unknown",
                "Duration": "35 seconds",
                "Call Type": "Incoming",
            },
        ]

        st.dataframe(
            call_log,
            hide_index=True,
        )
