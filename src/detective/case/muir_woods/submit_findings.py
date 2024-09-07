"""A page to submit findings for the Muir Woods case."""

import streamlit as st
from case.muir_woods.victim_profiles import victim_profile_map
from utils.openai import get_openai_full_response
import pandas as pd

st.title("🔍 Submit Findings")

st.markdown(
    """
    > Ensure you've cross-checked the goals / objectives with Lestrade. Lestrade will review your submission and provide feedback.    
    ---
"""
)

information_for_findings = """
 - You don't need smoking guns, just viable links b/w the victims and possible perps to further the investigation.
 - If you have evidence supporting homicide, but not of the perp, leave the `Perpetrator` column blank.
 - If you think multiple victims were involved in one common denominator other than a potential perpetrator, such as someone / something, mention that in the `Next Lead` column. The most occuring `Next Lead` will be up next for investigation in Phase 2. 
 - If there are no "Next Leads", mention `No Leads` on both leads columns.
"""

st.caption(information_for_findings)

st.info("Edit the table below and click `Submit` to review your case.")

review_df = st.data_editor(
    data=[
        {
            "Victim": victim_name,
            "Homicide": False,
            "Likely Perpetrator": "",
            "Perp vs. Victim Link": "",
            "Next Lead": "",
            "Link b/w Victim & Next Lead": "",
        }
        for victim_name in list(victim_profile_map.keys())
        if victim_name != "Home"
    ]
)

st.warning("This feature is still being refined, and the model may not always provide accurate feedback.")

lestrade_success_message = """
Great work team! You've not only successfully identifed that these were Homicides, but provided reasonable
evidence to support that Marco killed most, if not all of them. 

You've also done well to identify the link between the victims and the next lead: **The Gambolini Family**

I've just received DNA test results from the victims, and it appears that Melanie Sanders & Arthur Brane were illegitimate children of the deceased Gambolini patriarch.

Santino Gambolini now heads the family, with his wife Theresa. Their sister Alysayne and younger brother Nathan are also part of the family business.

We'll investigate the Gambolinis in Phase 2, where you'll be able to interrogate them directly (Coming Soon). 
"""

if st.button("Submit"):
    correct_responses = pd.read_csv(
        "src/detective/data/muir_woods_geography/correct_responses_to_muir.csv"
    )

    review_prompt = f"""
    You are detective inspector Lestrade overseeing the Muir Woods case. 
    You've received a submission from your team with some findings. 

    WHAT TO DO:
    - Cross reference their submission below with the "Correct Submission" below and provide feedback to your investigators. 
    - If they provide brief but accurate responses with strong evidence that's mentioned in the same context in "Correct Responses", you may approve their findings. 
    - If they provide valid responses for some but not other victims, you can validate the correct responses and ask for more information on the others.
    - If they provide an incomplete response, ask for more information without revealing what they should be looking for.
    
    WHAT NOT TO DO:
    
    - NEVER tell them specifics about something they missed, by providing the correct answer. Never ask them to check a connection which they haven't made already.
    - You cannot let them know in any way that there's a "Correct Submission" to cross-reference with.
    - You cannot tell them the answer but ask for missing links related to certain evidence not accounted for using the correct response as reference. 
    - Never give away information from "Correct Submission" when providing feedback if your team misses something.
    - Do not focus any part of your feedback on Motive, or asking more than the connections described in "Correct Submission".
    - Do not ask for data that is not present for that particular victim in the "Correct Submission".
    - Do not ask for data that is NULL in the "Correct Submission".
    - You don't need to be overly pedantic about details. If they show strong connections with large overlaps to the "Correct Submission", you can approve their findings, even if they miss a few details.

    If your team has provided a correct submission, you may provide them with the following success message. Do not change it any way, but include emojis to celebrate.:
    {lestrade_success_message}

    - Keep your response brief at a maximum of 150 words. You may use markdown in your response.
    ---
    CORRECT SUBMISSION:
    {correct_responses}

    ---
    SUBMITTED BY YOUR TEAM:
    {pd.DataFrame(review_df)}
    """
    st.caption("🕵🏼‍♂️ Lestrade's Response:")
    response = get_openai_full_response(review_prompt, model="gpt-4o")

    if (
        response
        and "santino gambolini" in response.lower()
        and "coming soon" in response.lower()
    ):
        st.success(lestrade_success_message)
        st.balloons()
        st.info("You've successfully completed the Muir Woods case. 🎉")
        st.success("Share [**muirwoods.streamlit.app**](https://muirwoods.streamlit.app) on social media to challenge your friends!")
    else:
        st.write(response)
