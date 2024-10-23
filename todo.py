import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from a file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("Your Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def add_task(tasks, task):
    """Add a new task."""
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def delete_task(tasks, task_index):
    """Delete a task by index."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task index.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                delete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
