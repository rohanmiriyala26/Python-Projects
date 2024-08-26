tasks = []
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")
def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the list.")
def show_tasks():
    if tasks:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks found.")
def complete_task():
    task = input("Enter the task to mark as complete: ")
    if task in tasks:
        tasks.remove(task)
        print("Task completed and removed from the list.")
    else:
        print("Task not found in the list.")
def show_menu():
    print("Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Mark a task as complete")
    print("5. Exit")
def tdl():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
tdl()
