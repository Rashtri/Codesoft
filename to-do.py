import sys

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Added task: '{task}'")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for index, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"Task '{self.tasks[index]['task']}' marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"Deleted task: '{task['task']}'")
        else:
            print("Invalid task number.")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            print(f"Updated task number {index + 1} to '{new_task}'")
        else:
            print("Invalid task number.")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Update task")
    print("6. Exit")

def main():
    app = TodoApp()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task description: ")
            app.add_task(task)
        elif choice == '2':
            app.list_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as done: ")) - 1
            app.mark_task_done(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: ")) - 1
            app.delete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task description: ")
            app.update_task(task_number, new_task)
        elif choice == '6':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
