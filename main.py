# To-Do List App
import os

def display_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    

def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    return []

def save_tasks(file_path, tasks):
    with open(file_path, "w") as file:
        file.write("\n".join(tasks))

def main():
    file_path = "tasks.txt"
    tasks = load_tasks(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYour Tasks:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found!")
        elif choice == "2":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(file_path, tasks)
            print("Task added successfully!")
        elif choice == "3":
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                save_tasks(file_path, tasks)
                print("Task removed successfully!")
            else:
                print("Invalid task number!")
        elif choice == "4":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")
            
        

if __name__ == "__main__":
    main()