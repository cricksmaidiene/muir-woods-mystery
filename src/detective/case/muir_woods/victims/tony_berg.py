"""Tony Bergenthal's victim profile data"""

import streamlit as st


def get_tony_berg_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "27")
    time_of_death.metric("Time of Death", "9.31 PM")
    origin_location.metric("Origin", "Sausalito, CA")

    st.caption("Cause of Death")
    st.error("Self-inflicted poisoning")

    st.json(
        {
            "Occupation": "Staff software engineer at Databricks.",
            "Marital Status": "Single",
            "Children": None,
            "Last Known Whereabouts": None,
        }
    )

    with st.expander("### Background"):
        st.caption(
            """
        - **Occupation:** Tony Bergenthal was a software engineer working at Databricks in their San Francisco office, specializing in scaling Databricks' serverless compute offering to millions of users. Known for his innovative thinking and problem-solving skills, he had a deep passion for technology.

        - **Personality:** Tony was the more laid-back and easygoing sibling compared to Sarah. He had a love for the local tech scene and often attended meetups and hackathons in the Bay Area. He was a die-hard Led Zeppellin fan, with "Stairway to Heaven" being his favorite song.

        - **Sausalito:** Like his sister, Tony was born and raised in Sausalito. He loved the blend of small-town charm and proximity to the tech hubs of the Bay Area. Tony was known to frequent the local coffee shop where he enjoyed a strong brew and catching up with friends or brainstorming new project ideas.

        - **Relationships:** Tony was close to his sister, Sarah, and her death deeply affected him. Distraught by the loss, Tony became consumed with finding answers, even going so far as to conduct his own investigation into her death. His determination to uncover the truth ultimately led him to the campsite where his life ended.
        """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error(
            "Poisoning due to high levels of formic acid in bloodstream and digestive tracts."
        )

        st.caption("### Details on Time of Death")
        st.caption(
            """
            - **Apparent Cause:** Tony was found deceased at a campsite near Sausalito. The initial cause of death was attributed to poisoning, possibly from consuming wild plants or contaminated food. The scene showed no signs of struggle.

            - **Unnoticed Clues:** After a more thorough investigation, faint traces of an unusual substance were found on his belongings. Additionally, a small puncture mark on his arm was discovered.

            Likely consumed the poison around 9.00 PM, leading to rapid deterioration of health and eventual death. The poison was ingested, and the effects were quick-acting, causing severe pain and respiratory distress. The exact source of the poison is still under investigation.
            Formic acid has high levels of Methanol which lead to shock and then death.
        """
        )

    with st.expander("### Tony's Investigation Log"):
        st.markdown(
            """
| **Date** | **Entry** | **Summary**| 
|---|---|---| 
| 7 days ago    | "I can’t shake the feeling that Sarah’s death wasn’t an accident."                                         | Noticed a bruise on Sarah's elbow in the coroner's photos. The placement seems odd for drowning face-first in the creek. The investigators say she would have need to hit it against a very hard object, but the location of the bruise is uncommon. Not the kind cause by a tree branch, or a fall for instance.  |
| 5 days ago    | "Started researching drowning injuries—this bruise doesn’t add up. The only mode by which the elbow could have been bruised where it was is if she was willingly trying to knock something (or someone) with her elbow."                                        | After researching, Tony found that the bruise on Sarah’s elbow is inconsistent with typical drowning injuries |
| 1 day ago | "Got a tip from a local as I was randomly walking down Elm lane today. The man had a hoodie on, but I could make out a tattoo of some sort down his neck as he turned. He told me to ask the morgue assistant for more details about his sister and also mentioned looking for evidence of a struggle in the woods, specifically areas that are easy to ambush from very close to Sarah's location. He mentioned that it's best to check after 8.00pm." | Tony goes onto mention that it was very odd for someone to give him a tip like this, but he was unable to follow up with the stranger and never met him since |
| 1 day ago    | "Visited the morgue—got an opinion from someone who knows."                                                | Spoke with a morgue assistant who unofficially confirmed that the bruise looks like it came from a struggle, not a fall. She would have had to fall backwards on her elbow right on some rocks, or otherwise have "elbowed" someone (probably on the bone) for there to be bruising such as this. Tony is now convinced Sarah was force-drowned, and tried to defend herself as she was being restrained by back-jolting her hand on the perpetrator. |
                    """
        )
