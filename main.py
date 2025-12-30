tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def menu():
    print("\n1. Add Task")
    print("2. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        break
    else:
        print("Invalid choice")
