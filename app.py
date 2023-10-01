import streamlit as st
from src.helpers import customStyle

st.set_page_config(
    page_title="You shouldn't be here!",
    page_icon=":warning:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if __name__ == '__main__':
    st.title("You shouldn't be here!")
    st.write("Are you trying to reverse engineer my app? \n")

    st.write("If you are, you're in luck! I've made the code available on GitHub:)")
    st.write("https://github.com/julien040/blog-embed")
    customStyle()
