import FreeSimpleGUI as sg
import functions
import time

sg.theme('LightBrown6')
now = sg.Text('', key='clock')
label = sg.Text('Enter Task:')
input_field = sg.InputText(tooltip="Enter task", key="task")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.read_tasks(), key="tasks", enable_events=True, size=[25, 10])
edit_button = sg.Button('Edit')
done_button = sg.Button('Done?')

window = sg.Window(title='Worknote',
                   layout=[[now],
                           [label],
                           [input_field, add_button],
                           [list_box,edit_button,done_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED:
        break

    window['clock'].update(time.strftime('%b %d, %Y %H:%M:%S'))
    print(event, values)

    match event:
        case 'Add':
            tasks = functions.read_tasks()
            if values['task'] != '':
                new_task = values['task'] + "\n"
                tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case 'Edit':
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task'] + "\n"
                tasks = functions.read_tasks()
                idx = tasks.index(task_to_edit)
                tasks[idx] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
            except IndexError:
                sg.popup_error('Please enter a task first', font='Helvetica')

        case 'Done?':
            try:
                task_to_delete = values['tasks'][0]
                tasks = functions.read_tasks()
                tasks.remove(task_to_delete)
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)

            except IndexError:
                sg.popup_error('Please enter a task first', font='Helvetica')





window.close()