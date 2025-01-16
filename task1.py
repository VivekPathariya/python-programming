import json

# Task storage
tasks = []

# Function to add a new task
def add_task(title):
    task = {"title": title, "completed": False}
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['title']} - {status}")

# Function to mark a task as completed
def mark_task_completed(index):
    try:
        tasks[index - 1]["completed"] = True
        print(f"Task {index} marked as completed!")
    except IndexError:
        print("Invalid task number!")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Main program loop
load_tasks()  # Load tasks from file at the start
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":  # Add Task
        title = input("Enter task title: ")
        add_task(title)
    elif choice == "2":  # List Tasks
        list_tasks()
    elif choice == "3":  # Mark Task as Completed
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            mark_task_completed(task_num)
        except ValueError:
            print("Please enter a valid number!")
    elif choice == "4":  # Exit
        save_tasks()  # Save tasks before exiting
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
        
        
        
