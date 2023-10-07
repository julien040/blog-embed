import streamlit as st
from src.github.getRepoSize import getRepoSize
from src.helpers import customStyle, humanbytes


st.set_page_config(
    page_title="GitHub Repository Size",
    page_icon=":warning:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

customStyle()


url = st.experimental_get_query_params().get("url", [""])[0]

try:
    size = getRepoSize(url)
    st.markdown(
        """
    <style>
    [data-testid="stText"]{
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        font-family: sans-serif;

    }
    """, unsafe_allow_html=True)
    st.text(humanbytes(size))
except Exception as e:
    st.error(e)
