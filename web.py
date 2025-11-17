import streamlit as st
import functions

tasks = functions.read_tasks()

def add_task():
    task = st.session_state['new_task'] + '\n'
    tasks.append(task)
    functions.write_tasks(tasks)

st.title('Worknote')
st.subheader('Your Efficiency Solution')
st.write('Your tasks')

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input(label='', placeholder='Enter a task',
              on_change=add_task, key='new_task')