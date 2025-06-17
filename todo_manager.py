import os
tasks = []

def load_tasks_from_file(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    title, description, due_date, done = line.strip().split("|")
                    tasks.append({
                        "title": title,
                        "description": description,
                        "due_date": due_date,
                        "done": done == "True"
                    })
                except ValueError:
                    print(f"Skipped malformed line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new one.")
        open(filename, "w").close()
    except PermissionError:
        print(f"Permission denied for '{filename}'.")

def save_tasks_to_file(filename="tasks.txt"):
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(f"{task['title']}|{task['description']}|{task['due_date']}|{task['done']}\n")
        print(f"Tasks saved to '{filename}'")
    except Exception as e:
        print(f"Failed to save tasks: {e}")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task = {"title": title, "description": description, "due_date": due_date, "done": False}
    tasks.append(task)
    save_tasks_to_file()
    print(f"Task '{title}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "[✓]" if task['done'] else "[ ]"
        print(f"{idx}. {status} {task['title']} (Due: {task['due_date']}) - {task['description']}")
    print("\nYou can also view the list of tasks in 'tasks.txt'")

def mark_task_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['done'] = True
            save_tasks_to_file()
            print(f"Marked task '{tasks[index - 1]['title']}' as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks_to_file()
            print(f"Removed task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    load_tasks_from_file()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting To-Do Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
