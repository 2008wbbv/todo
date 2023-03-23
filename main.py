tasks = []

def addtask():
    taskname = input("add a task: ")
    tasks.append(taskname)
    print("--------------------------------------------------------------------")
    print("task added")
def removetask():
    task_name = input("Enter task name: ")
    if task_name in tasks:
        tasks.remove(task_name)
        print("Task deleted.")
    else:
        print("Task not found.")
def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
while True:
    print("Menu:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Display tasks")
    print("4. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")