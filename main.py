import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task():
    title = input("Task title: ")
    description = input("Description: ")
    due_date = input("Due date (YYYY-MM-DD): ")
    priority = input("Priority (High/Medium/Low): ")

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# List tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['title']} (Due: {task['due_date']}, Priority: {task['priority']})")

# Mark task as completed
def mark_complete():
    list_tasks()
    tasks = load_tasks()
    try:
        idx = int(input("Enter task number to mark as completed: ")) - 1
        tasks[idx]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except:
        print("Invalid task number.")

# Delete a task
def delete_task():
    list_tasks()
    tasks = load_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        deleted = tasks.pop(idx)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {deleted['title']}")
    except:
        print("Invalid task number.")

# Menu
def main():
    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
