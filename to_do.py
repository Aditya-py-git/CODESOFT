# Simple To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ No tasks in the list.\n")
    else:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✔ Task '{task}' added!\n")

def remove_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"❌ Task '{removed}' removed!\n")
        except (ValueError, IndexError):
            print("⚠ Invalid task number.\n")

def main():
    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
