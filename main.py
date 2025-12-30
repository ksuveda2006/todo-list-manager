tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    print(tasks[0]["task"])   # ❌ BUG: crashes if list is empty

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
