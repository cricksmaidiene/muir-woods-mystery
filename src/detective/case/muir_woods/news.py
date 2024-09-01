import streamlit as st

st.header("Extra, Extra, Extra! Read all about it! 🗞")

with st.expander("### Internet Troll Takes Center Stage Amid Muir Woods Mystery"):
    st.image("src/detective/data/news/arjuan.png")

    with open("src/detective/docs/muir_woods/news/internet_troll.md", "r") as f:
        st.markdown(f.read())

with st.expander("### Start-up Duo Raises $20M Pre-Seed for Revolutionary 'Cloud Farming'"):
    st.image("src/detective/data/news/kelvin_mateo.jpg")

    with open("src/detective/docs/muir_woods/news/startup.md", "r") as f:
        st.markdown(f.read())

with st.expander("""### Florida Man Reflects on San Francisco Trip: "It’s Like the Ocean, But Fancier"""):
    st.image("src/detective/data/news/nuno.png")

    with open("src/detective/docs/muir_woods/news/florida.md", "r") as f:
        st.markdown(f.read())