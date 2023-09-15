import functions
import PySimpleGUI as sg

label = sg.Text("Type in a text")
input_box = sg.InputText(tooltip='enter a text',key='todo')
add_button = sg.Button("Add")
del_but = sg.Button("delete")
list_box=sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True,
                    size=[10, 10])
edit_but=sg.Button("Edit")
window = sg.Window('APP BY SAIYAN',
                   layout=[[label, input_box, add_button],
                           [list_box,edit_but],[del_but]],
                   font=("Helvetica", 20))

while True:
    events, values = window.read()
    print(1,events)
    print(2,values)
    match events:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.writing_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
