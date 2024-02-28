class ToDoList:
    def __init__(self):
        self.tasks = []     # List which stores all the tasks in the to-do list

    # Adding a task into the to-do list
    def add_task(self, task):
        self.tasks.append(task)     # Appends a task to the end of the list
        print("Your task added successfully!")

    # Removing the required task from the list
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)        # If the task you want to delete is present in the list, then remove that task from the to-do list
            print("Task removed successfully!")
        else:
            print("Task not found!")        # If the required task is not present in the to-do list, then print this message

    # Displaying the list of all the tasks present in to-do list along with their indices
    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):   # Iterating over the list of all in self.tasks to generate the indices for the tasks starting from 1
                print(f"{idx}. {task}")                        # printing the tasks along with their indices
        else:
            print("Your ToDoList is empty!")

    # Updating the required task in the list
    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            idx = self.tasks.index(old_task)
            self.tasks[idx] = new_task
            print("Your task updated successfully!")
        else:
            print("Task not found!")


def main():
    todo_list = ToDoList()    # creating an object to the class ToDoList

    while True:
        print("\n      TODOLIST MENU:")
        print("***************************")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display tasks")
        print("4. Update the task")
        print("5. Exit")
        print("****************************")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice :) Please enter your choice between 1 and 5.")


if __name__ == "__main__":
    main()
