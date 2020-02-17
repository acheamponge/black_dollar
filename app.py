import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.about
import src.pages.analytics
import src.pages.analytics1
import src.pages.analytics2
import src.pages.analytics3
import src.pages.resources

MENU = {
    "Home" : src.pages.home,
    "Employment Data" : src.pages.analytics,
    "Unemployment Data" : src.pages.analytics1,
    "Labor Force Data" : src.pages.analytics2,
    "Home ownership Data" : src.pages.analytics3,
    "Resources" : src.pages.resources,
    "About" : src.pages.about
}

def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Pick an option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)

    st.sidebar.title("Contribute")
    st.sidebar.info(
        "This an open source project and please feel free to contribute"
        +"\n"+
        "[Github](https://github.com/acheamponge/black_dollar)"
        +"\n"+
        "\n"+
        "[Google Docs](https://docs.google.com/document/d/1hU56Ztl10B-B3xqNjOXMvZ2GIh_h07aUm_yx5Ra08pA/edit?usp=sharing) "
    )
    
      
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This purpose of this app is to create an interactive platform to analyze the economic data of African Americans from the Federal Reserve Bank of St. Louis."""
    )
    
    st.sidebar.title("Special Thanks")
    st.sidebar.info(
        "Huge thank you to MarcSkovMadsen and Avkash whose use of Streamlit helped make the webapp for this project"
        +"\n"+
        "[MarcSkovMadsen](https://github.com/MarcSkovMadsen/awesome-streamlit/)"
        +"\n"+"\n"+
        "[Avkash](https://github.com/Avkash/demoapps) "
        )

if __name__ == "__main__":
    main()