"""
To-Do List Application
-----------------------
A simple command-line To-Do List manager built in Python.
Tasks are saved to a JSON file so your list persists between runs.

Features:
- Add a task
- View all tasks
- Update/edit a task
- Mark a task as complete
- Delete a task
- Tasks are saved automatically to tasks.json
"""

import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("\nYour to-do list is empty!\n")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "✘ Pending"
        print(f"{i}. {task['title']}  [{status}]")
    print("-----------------------\n")


def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter the task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Task '{title}' added successfully!\n")
    else:
        print("Task description cannot be empty.\n")


def update_task(tasks):
    """Edit the text of an existing task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to update: "))
        if 1 <= num <= len(tasks):
            new_title = input("Enter the new task description: ").strip()
            if new_title:
                tasks[num - 1]["title"] = new_title
                save_tasks(tasks)
                print("Task updated successfully!\n")
            else:
                print("Task description cannot be empty.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def mark_complete(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    menu = """
=========================
      TO-DO LIST APP
=========================
1. View tasks
2. Add task
3. Update task
4. Mark task as complete
5. Delete task
6. Exit
=========================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
