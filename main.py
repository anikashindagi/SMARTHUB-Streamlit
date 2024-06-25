import streamlit as st
from streamlit_option_menu import option_menu
import home
import contactt
import dailytask
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="SMART HUB!",page_icon=':blue heart:')


rain(
    emoji="✨",
    font_size=20,
    falling_speed=5,
    animation_length="10"
)
def main():
    with st.sidebar:
        selected = option_menu(
            menu_title='SMART-HUB!!',
            options=['Home', 'Contact Book', 'Daily Task Tracker'],
            icons=['house','phone','check'],
            default_index=0,
        )
    
    if selected == "Home":
        home.app()
    elif selected == "Contact Book":
        contactt.app()
    elif selected == "Daily Task Tracker":
        dailytask.app()

if __name__ == "__main__":
    main()