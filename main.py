tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["completed"] else "✗"
        print(f"{i}. {t['task']} [{status}]")

def mark_complete():
    view_tasks()
    index = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
