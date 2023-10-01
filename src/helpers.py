from streamlit import markdown


def customStyle():
    markdown(
        """
        <style>
        div[data-testid="collapsedControl"]
        {
            display: none !important;
        }

        footer {visibility: hidden;}


        </style>


    """, unsafe_allow_html=True)
