import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    # Create columns for side-by-side layout
    col1, col2 = st.columns([2, 3])

    with col1:
        st.title("Welcome to SMART HUB")
        st.write("Leading life a better and organized way!")
        st.write('There are 2 options included in this website:')
        st.write('---')
        st.write("### Contact List")
        st.write("Add, view, and delete contacts!")
        st.write("### Daily Task Planner")
        st.write("Enter and delete tasks!")

    with col2:
        lott = load_lottie("https://lottie.host/d1555005-d086-4dca-a499-dad07c679bb9/ZMcJzOwD0q.json")
        if lott:
            st_lottie(lott, speed=1, loop=True, height=600, width=450)

if __name__ == "__main__":
    app()
