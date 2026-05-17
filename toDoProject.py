import os
task_file = "list.txt"
def load_tasks():
    if not os.path.exists(task_file):
        return []
    with open(task_file,'r') as file:
        return [task.strip() for task in file.readlines()]
def save_task(tasks):
    with open(task_file,'w') as file:
        for task in tasks:
            file.write(task+ '\n')
def add_task():
    task = input("Enter the task:")
    tasks = load_tasks()
    tasks.append(task)
    save_task(tasks)
    print("Task added successfully\n")
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No Tasks found!\n")
    else:
        print("Your To - Do List-")
        for i,task in enumerate(tasks,1):
            print(i,".",task)
def update_task():
    view_tasks()
    tasks = load_tasks()
    try:
        index = int(input("Enter the task number to update:"))-1
        if 0 <= index < len(tasks):
            new_task = input("Enter your new task:")
            tasks[index] = new_task
            save_task(tasks)
            print("Your task is updated\n")
    except ValueError:
        print("Invalid value, please enter valid value\n")
def delete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        index = int(input("Enter the task number to delete:"))-1
        if 0<=index<len(tasks):
            tasks.pop(index)
            save_task(tasks)
            print("Successfully deleted the task\n")
        else:
            print("Enter valid index\n")
    except ValueError:
        print("Invalid value, please enter valid value to delete the task\n")
def clearall_tasks():
    tasks = load_tasks()
    tasks = []
    save_task(tasks)
    print("All the tasks has been successfully cleared\n")

while True:
    print("========================================================")
    print("1.Create Task\n2.View Task\n3.Update Task\n4.Delete Task\n5.Clear All Tasks\n6.Exit\n")
    try:
        op = int(input("Enter the option to be performed:"))
        if(op == 6):
            break
        match op:
            case 1:
                add_task()
            case 2:
                view_tasks()
            case 3:
                update_task()
            case 4:
                delete_task()
            case 5:
                clearall_tasks()
            case _:
                print("Enter valid operation number")
    except ValueError:
        print("Please enter a valid index")



