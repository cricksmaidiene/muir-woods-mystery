"""Sarah Bergenthal's victim profile data"""

import streamlit as st


def get_sarah_data():
    age_metric, time_of_death, origin_location = st.columns(3)
    age_metric.metric("Age", "29")
    time_of_death.metric("Time of Death", "4.47 PM")
    origin_location.metric("Origin", "Sausalito, CA")

    st.caption("Cause of Death")
    st.error("Alleged Drowning")

    st.json(
        {
            "Occupation": "Astrophysicist & Applied Mathematics PhD at University of California, Berkeley",
            "Marital Status": "Single",
            "Children": None,
            "Last Known Whereabouts": None,
        }
    )

    with st.expander("### Background"):
        st.caption(
            """
        - **Occupation:** Sarah Bergenthal was a rising star in the field of astrophysics, working as a researcher at UC Berkeley. Known for her passion for the stars, Sarah was deeply committed to her work, often spending long hours at the observatory. Her research focused on the search for exoplanets, and she had recently been published in a prominent scientific journal.

        - **Personality:** Sarah was a curious and driven individual. She was known for her sharp intellect and had a reputation for being both dedicated and approachable. Despite her busy academic life, she made time to visit her hometown of Sausalito regularly, where she enjoyed the quiet escape from the city. Locals often saw her enjoying a scoop of salted ice cream from her favorite shop by the waterfront.

        - **Connection to Sausalito:** Born and raised in Sausalito, Sarah maintained close ties to the community. She often returned home to visit her younger brother, Tony, and catch up with old friends. Sarah’s love for the area was well known—she frequently posted pictures of the Sausalito sunset on her social media.

        - **Hobbies:** Outside of her work, Sarah enjoyed hiking, photography, and stargazing. She was often seen with her camera, capturing moments of natural beauty. She had a close-knit circle of friends from Berkeley and UCSF and frequently met them for coffee and long discussions about science and the meaning of life, often discussing Fermi's paradox.

        - **Relationships:** Sarah was close to her brother, Tony, who also lived in Sausalito. Though their lives had taken different paths, they remained in regular contact. Tony often joked that he lived in Sarah's shadow, but he was deeply proud of her achievements.
        """
        )

    with st.expander("### Coroner's Report"):
        st.caption("### Cause of Death")
        st.error("Drowning")

        st.caption("### Details on Time of Death")
        st.caption(
            """
            Sarah was found drowned in a creek near Sausalito. Faint bruising on her right arm. The initial investigation suggested that she may have slipped and fallen into the water during a hike. There were no obvious signs of foul play.
        """
        )

    with st.expander("### Whereabouts & Witness Statements"):
        st.caption("Tony Bergenthal's Statement")
        st.caption(
            """
            ```markdown
            Sarah was always the brilliant one—the one who reached for the stars, 
            literally. I can't believe she's gone. 
            It doesn’t make sense. She knew those trails like the back of her hand; 
            she wasn’t reckless. There’s no way this was just an accident. 
            I’ve lost my sister, my best friend, and I can’t shake the feeling that 
            something’s not right. I need to find out what 
            happened to her—I owe her that much.
            ```
            """
        )

    with st.expander("### Sarah's Social Media Feed"):
        st.caption(
            "Sarah was a bit of a social media mini-celebrity in the science community. Here are some of her recent posts:"
        )
        social_media_data = [
            {
                "Time of Post": "14 days ago",
                "Post Caption": "Just published my latest paper on exoplanets! Feeling grateful for the support from my colleagues at Berkeley. 🌟🚀",
                "Comments Summary": "Congratulatory comments from colleagues and friends.",
                "Image": "https://images.unsplash.com/photo-1532153955177-f59af40d6472?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            },
            {
                "Time of Post": "13 days ago",
                "Post Caption": "Nothing like stargazing to clear the mind. The universe is endless, and it's beautiful. ✨🌌",
                "Comments Summary": "Comments about how stunning the photo is, suggestions for new stargazing spots.",
                "Image": "https://plus.unsplash.com/premium_photo-1661277679965-9db1104e890f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bWlsa3klMjB3YXl8ZW58MHx8MHx8fDA%3D",
            },
            {
                "Time of Post": "10 days ago",
                "Post Caption": "Work can be exhausting, but there's always time for a quick hike. Thinking of heading to Muir Woods this weekend. 🌲🍃",
                "Comments Summary": "Friends recommending trails and asking to join.",
                "Image": "https://images.unsplash.com/photo-1528306606980-c7b093f99f21?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bXVpciUyMHdvb2RzfGVufDB8fDB8fHww",
            },
            {
                "Time of Post": "7 days ago",
                "Post Caption": "Sausalito sunsets never get old. 🌅 I miss this view when I'm at Berkeley.",
                "Comments Summary": "Comments from locals reminiscing about Sausalito and favorite spots.",
                "Image": "https://live.staticflickr.com/5204/5325951063_ae2230e343_b.jpg",
            },
            {
                "Time of Post": "5 days ago",
                "Post Caption": "Excited to finally take a break and spend a day in nature. Thinking of hitting the trail tomorrow morning. Anyone have suggestions for a good hike?",
                "Comments Summary": "Recommendations for Muir Woods, with some comments suggesting specific spots like the creek area.",
                "Image": "https://plus.unsplash.com/premium_photo-1711255560433-60dafe53f76d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cmFpbnklMjB3b29kc3xlbnwwfHwwfHx8MA%3D%3D",
            },
            {
                "Time of Post": "4 days ago",
                "Post Caption": "Nature day! Heading to Muir Woods for a solo hike. Plan to start at the main trailhead and loop around the creek—should be peaceful. 🌿",
                "Comments Summary": "Comments wishing her a good hike, suggesting she check out certain overlooks along the way.",
                "Image": "https://plus.unsplash.com/premium_photo-1690574169354-d6cc4299cf84?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8aGlraW5nfGVufDB8fDB8fHww",
            },
            {
                "Time of Post": "3 days ago",
                "Post Caption": "Another beautiful night in Sausalito. I needed this after a long day.",
                "Comments Summary": "Supportive comments, friends asking if she’s okay.",
                "Image": "https://images.unsplash.com/photo-1631258578554-75acc38b6f99?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c2F1c2FsaXRvJTIwc2t5bGluZXxlbnwwfHwwfHx8MA%3D%3D",
            },
            {
                "Time of Post": "2 days ago",
                "Post Caption": "Back to work at Berkeley tomorrow, but tonight, it's all about the stars. 🌠",
                "Comments Summary": "Comments about how peaceful her stargazing looks in other posts, people asking about her research.",
                "Image": "https://images.unsplash.com/photo-1671709362458-53c8354565b9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8YmVya2VsZXl8ZW58MHx8MHx8fDA%3D",
            },
            {
                "Time of Post": "1 day ago",
                "Post Caption": "So grateful for the simple moments. Sometimes, a quiet night in Sausalito is all you need.",
                "Comments Summary": "Friends commenting on how cozy it looks, asking for book recommendations.",
                "Image": "https://plus.unsplash.com/premium_photo-1679404108270-71b22febf4f2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Ym9vayUyMGNvZmZlZXxlbnwwfHwwfHx8MA%3D%3D",
            },
            {
                "Time of Post": "Day of Death",
                "Post Caption": "Off to explore the trails again today. Starting at the creek trail—should be a quiet hike. 🌲",
                "Comments Summary": "Comments suggesting scenic spots along the trail, wishing her a peaceful hike.",
                "Image": "https://images.unsplash.com/photo-1472740378865-80aab8e73251?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8bXVpciUyMHdvb2RzfGVufDB8fDB8fHww",
            },
        ]

        st.dataframe(
            social_media_data,
            hide_index=True,
            column_config={"Image": st.column_config.ImageColumn("Image")},
        )
