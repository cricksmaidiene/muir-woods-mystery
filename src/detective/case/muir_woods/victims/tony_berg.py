"""Tony Bergenthal's victim profile data"""

import streamlit as st


def get_tony_berg_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "27")
    time_of_death.metric("Time of Death", "9.31 PM")
    origin_location.metric("Origin", "Sausalito, CA")

    st.caption("Cause of Death")
    st.error("Poisoning")

    st.json(
        {
            "Occupation": "Staff software engineer at Databricks.",
            "Marital Status": "Single",
            "Children": None,
            "Last Known Whereabouts": None
        }
    )

    with st.expander("### Background"):
        st.caption(
            """
        - **Occupation:** Tony Bergenthal was a software engineer working at Databricks in their San Francisco office, specializing in scaling Databricks' serverless compute offering to millions of users. Known for his innovative thinking and problem-solving skills, Tony was a valued member of his team. He had a deep passion for technology and was always eager to take on new challenges in his work.

        - **Personality:** Tony was the more laid-back and easygoing sibling compared to Sarah. He was known for his sense of humor and his ability to keep things light, even during stressful situations. Despite his relaxed demeanor, Tony was highly focused and driven when it came to his work. He had a love for the local tech scene and often attended meetups and hackathons in the Bay Area. He was a die-hard Led Zeppellin fan, with "Stairway to Heaven" being his favorite song.

        - **Sausalito:** Like his sister, Tony was born and raised in Sausalito. He loved the blend of small-town charm and proximity to the tech hubs of the Bay Area. Tony was known to frequent the local coffee shop where he enjoyed a strong brew and catching up with friends or brainstorming new project ideas.

        - **Hobbies:** Tony was an avid gamer and enjoyed outdoor activities, often blending his love for technology with his passion for nature. He regularly camped in the area, finding it a peaceful escape from the fast-paced world of software development and AI-driven stakeholders.

        - **Relationships:** Tony was close to his sister, Sarah, and her death deeply affected him. Distraught by the loss, Tony became consumed with finding answers, even going so far as to conduct his own investigation into her death. His determination to uncover the truth ultimately led him to the campsite where his life ended.
        """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error("Poisoning due to high levels of formic acid in bloodstream and digestive tracts.")

        st.caption("### Details on Time of Death")
        st.caption(
            """
            - **Apparent Cause:** Tony was found deceased at a campsite near Sausalito. The initial cause of death was attributed to poisoning, possibly from consuming wild plants or contaminated food. The scene showed no signs of struggle, and his death was initially ruled accidental.

            - **Unnoticed Clues:** After a more thorough investigation, faint traces of an unusual substance were found on his belongings. Additionally, a small puncture mark on his arm was discovered.

            Likely consumed the poison around 9.00 PM, leading to rapid deterioration of health and eventual death. The poison was ingested, and the effects were quick-acting, causing severe pain and respiratory distress. The exact source of the poison is still under investigation.
            Formic acid has high levels of Methanol which lead to shock and then death.
        """
        )

    with st.expander("### Tony's Investigation Log"):
        st.markdown("""
| **Date**      | **Entry Summary**                                                                                         | **Details**                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 7 days ago    | "I can’t shake the feeling that Sarah’s death wasn’t an accident."                                         | Noticed a bruise on Sarah's elbow in the coroner's photos. The placement seems odd for a simple fall. The investigators say she would have need to hit it against a very hard object, but the location of the bruise is uncommon.  |
| 5 days ago    | "Started researching drowning injuries—this bruise doesn’t add up. The only mode by which the elbow could have been bruised where it was is if she was willingly trying to knock something (or someone) with her elbow."                                        | After researching, Tony found that the bruise on Sarah’s elbow is inconsistent with typical drowning injuries and seems more like the result of a non-accidental bump or scratch |
| 3 days ago    | "Visited the morgue—got an opinion from someone who knows."                                                | Spoke with a morgue assistant who unofficially confirmed that the bruise looks like it came from a struggle, not a fall. She would have had to fall backwards on her elbow right on some rocks, or otherwise have "elbowed" someone (probably on the bone) for there to be bruising such as this. Tony is now convinced Sarah was force-drowned. |
| 1 day ago     | "Retracing her steps—there’s something I’m missing."                                                      | Followed Sarah’s last hiking route, noting possible ambush points. He feels close to finding more evidence. |
| Day of Death  | "Heading back to the woods one last time. If I’m right, someone made sure she wouldn’t make it out alive." | Final entry before his death, believes he’s found enough to prove Sarah was murdered.                   |
                    """)