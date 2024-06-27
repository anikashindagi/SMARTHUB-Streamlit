import streamlit as st

def app():
    st.title("Let's assign you some tasks!")
    st.write("Please select your designation:")

    tasks = {
        "Learner": ["Study Python basics", "Complete a Python exercise", "Watch a Python tutorial"],"Applier": ["Build a small Python project", "Contribute to an open-source project", "Solve a real-world problem with Python"] }

    if 'seltasks' not in st.session_state:
        st.session_state.seltasks = {user_type: [] for user_type in tasks.keys()}
        
    col1,col2=st.columns(2)
    with col1:
        learner=st.checkbox("I am a Learner!")
    with col2:
        applier=st.checkbox("I am an Applier!")

    if learner:
        st.header("Learner Tasks are listed below-")
        for idx, task in enumerate(tasks["Learner"]):
            key = f"learner_task_{idx}"
            if st.checkbox(task, key=key):
                if task not in st.session_state.seltasks["Learner"]:
                    st.session_state.seltasks["Learner"].append(task)
            else:
                if task in st.session_state.seltasks["Learner"]:
                    st.session_state.seltasks["Learner"].remove(task)

    if applier:
        st.header("Applier Tasks are listed below-")
        for idx, task in enumerate(tasks["Applier"]):
            key = f"applier_task_{idx}"
            if st.checkbox(task, key=key):
                if task not in st.session_state.seltasks["Applier"]:
                    st.session_state.seltasks["Applier"].append(task)
            else:
                if task in st.session_state.seltasks["Applier"]:
                    st.session_state.seltasks["Applier"].remove(task)
    col1,col2=st.columns(2)
    st.header("Selected Tasks")
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.seltasks["Learner"]:
            st.subheader("Learner Accepted Tasks:")
            for task in st.session_state.seltasks["Learner"]:
                st.write(f"- {task}")

    with col2:
        if st.session_state.seltasks["Applier"]:
            st.subheader("Applier Accepted Tasks:")
            for task in st.session_state.seltasks["Applier"]:
                st.write(f"- {task}")
    
    if st.button("Click here to delete done tasks."):
     col1,col2=st.columns(2)
     with col1:
        if learner:
         st.write("Tasks deleted(Learner)-")
         donee=st.session_state.seltasks["Learner"]
         for task in donee:
                tasks["Learner"].remove(task)
                st.write(f"{task} deleted.")
     with col2:
        if applier:
         st.write("Tasks deleted(Applier)-")
         done=st.session_state.seltasks["Applier"]
         for task in done:
                tasks["Applier"].remove(task)
                st.write(f"{task} deleted.")
            
if __name__ == '__main__':
    app()