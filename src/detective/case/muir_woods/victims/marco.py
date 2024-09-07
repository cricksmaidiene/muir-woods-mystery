"""Marco's victim profile data"""

import streamlit as st


def get_marco_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "39")
    time_of_death.metric("Time of Death", "6.25 PM")
    origin_location.metric("Origin", "Columbus, OH")

    st.caption("Cause of Death")
    st.error("Gunshot wound to the head")

    st.json(
        {
            "Occupation": "Former Police Officer (Dishonorably Discharged)",
            "Marital Status": "Single, no known family",
            "Children": None,
            "Last Known Whereabouts": None,
        }
    )

    with st.expander("### Background"):
        st.success(
            """
            - **Height:** 6'1"
            - **Build:** Muscular, with a disciplined physique
            - **Distinctive Features:** Small scar under his left eye, a remnant from a training accident. A tattoo of his former unit’s insignia on his right shoulder.
            """
        )
        st.caption(
            """
        - **Occupation:** 
            - Sid Sangrevo was a former police officer who served outside of California. 
            - He had a long career in law enforcement, known for his dedication and skills, but his service ended abruptly when he was dishonorably discharged under controversial circumstances. 
            - The details of his discharge are sealed, but it is believed to be related to a case where excessive force was used.

        - **Personality:** 
            - Sid was known for his professionalism and strict adherence to discipline during his time in the force. 
            - However, after his discharge, he became reclusive, struggling to find purpose and financial stability. 
            - He had no known family or close connections, making him an isolated figure after his fall from grace.

        - **Skills:** 
            - Sid’s skills were honed through years of service in law enforcement. 
            - He was proficient in marksmanship, tactical operations, and survival techniques. 
            - His experience in handling high-pressure situations made him a formidable individual, even outside the force.

        - **Financial Status:** 
            - Sid was struggling financially, with no steady income or assets. 
            - His lifestyle was transient, moving from place to place in search of work.
  
        - **Social Connections:** 
            - Sid had no known family or close friends. 
            - His life after his discharge was solitary, and his interactions were limited to brief, transactional encounters.
        
        - **Surveillance Footage:** 
            - A security camera captured a blurry image of Sid at a gas station outside the Bay Area days before his death. 
            - This was the last known footage of him, and it offers no concrete details about his activities or intentions.
        """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error(
            "Gunshot wound to the head. The bullet entered through the back of the head, indicating that the victim was shot from behind. The bullet was found lodged in the frontal lobe, causing immediate death."
        )

        st.caption("### Details on Time of Death")
        st.caption(
            """
            Autopsy suggests that Marco and Arthur were killed within minutes of each other. It's not possible to determine who died first from biological evidence.
        """
        )

    with st.expander("### Whereabouts & Witness Statements"):
        st.caption(
            """
            - **Witness Statements:** No direct sightings of Sid were reported in the days leading up to his death.
            - **Travel History**: 
                - Sid flew into California on Delta's first-class cabin from Ohio just prior to the start of the murders. 
                - His return flight was booked for the morning after his body was discovered.
        """
        )

    with st.expander("### Evidence"):
        st.caption(
            """
            - **Clothing:** Sid was wearing his usual practical outdoor attire, including a weather-resistant coat and heavy-duty boots. Notably, he was also wearing gloves. His clothing showed signs of dirt and plant matter from the surrounding area
            - **Belongings**. The following were found on his person:
                - A small device, about the size of a deck of cards with buttons each labeled with obscure numerical ranges, and a small LED indicator light that flashes intermittently. The front face features a single, recessed button. On the back, there’s a retractable antenna. It emits a buzz that seems to cause network interference. Signs of wear suggesting it’s been used multiple times.
                - A note with cryptic instructions, partially obscured by water damage and tears. The note mentions a meeting at an overlook. The handwriting is difficult to decipher, but the note appears to be a set of instructions or a coded message.
                - An empty syringe, laced with residue of the same poisonous substance found in Tony Bergenthal's deceased body.
                - A couple smudged printouts of images printed of the woods and night sky, too blurry / torn up to make out any details.
        """
        )

        st.caption(
            """
            The following note was found crumpled inside Sid's socks. The ink has been smeared due to the mist, and holes in the paper make it hard to read. The note reads:

            ```
            …...et at… overlook … no later th… PM… n..w tar...s
            …will not a ain… ust be d..n… t muc… at st… ……an…e S……er…s & ..rth… ……an…e
            S.  G……oli…
            ```
            """
        )
