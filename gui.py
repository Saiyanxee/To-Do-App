import functions
import PySimpleGUI as sg

label = sg.Text("Type in a text")
input_box = sg.InputText(tooltip='enter a text',key='todo')
list_box=sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True,
                    size=[45, 10])
edit_but=sg.Button("Edit")
add_button = sg.Button("Add")
del_but = sg.Button("delete")

window = sg.Window('APP BY SAIYAN',
                   layout=[[label], [input_box, add_button],
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
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit=values['todos'][0]
            edited=values['todo']
            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=edited
            functions.writing_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
