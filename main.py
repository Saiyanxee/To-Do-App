import functions
import time

now=time.strftime("%b %d, %y, %H:%M:%S")
print("It is now",now)
print("the time is")
print("Todo App by Saiyan")

while True:
    user_action = input("type add,show,edit,complete or exit:")
    user_action = user_action.strip()
    # (.strip)is used to remove empty space after variable

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.writing_todos(todos)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            New_todo = input('enter the new todo')
            todos = functions.get_todos()
            todos[number] = New_todo + '\n'
            functions.writing_todos(todos)
        except ValueError:
            print("your command is wrong")
            continue
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.writing_todos(todos)
            message = f"todo {todo_to_remove} has been removed"
            print(message)
        except IndexError:
            print("enter valid value")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("enter a valid option")
print('exit.....')
