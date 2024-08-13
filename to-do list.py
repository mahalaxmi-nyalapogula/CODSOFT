def add_task(tasks):
    task_desc = input("Enter the task description: ")
    tasks.append({"description": task_desc, "completed": False})
    print(f'Task "{task_desc}" added.')

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f'{index}. {task["description"]} [{status}]')

def update_task(tasks):
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_desc = input("Enter the new description: ")
        tasks[task_number]["description"] = new_desc
        tasks[task_number]["completed"] = input("Is the task completed? (yes/no): ").lower() == "yes"
        print(f'Task {task_number + 1} updated.')
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f'Task "{removed_task["description"]}" deleted.')
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
