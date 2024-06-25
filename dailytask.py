import streamlit as st

def app():
    st.title("Daily Task Tracker welcomes you!")
    st.write("Keep a note of all your tasks---")

    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    task = st.text_input("Enter a task")

    if st.button("Add Task"):
        if task:
            st.session_state.tasks.append(task)
            st.success(f"Added task: {task}")

    st.write("### Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        col1.write(task)
        if col2.button("Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

