import tkinter as tkr
from tkinter import messagebox


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List") # Title displayed in title bar of the GUI window

        self.tasks = []  # List used for storing the tasks

        self.task_entry = tkr.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=30, pady=30)

        # Creating Add task button
        self.add_button = tkr.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=30, pady=30)

        # Creating a Listbox widget that displays tasks and positions it in the Tkinter window
        self.task_listbox = tkr.Listbox(root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=30, pady=30)

        # Creating Deleting task button
        self.delete_button = tkr.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=30, pady=30, sticky="W")

        # Creating Add Clear All button
        self.clear_button = tkr.Button(root, text="Clear All", command=self.clear_all_tasks)
        self.clear_button.grid(row=2, column=1, padx=30, pady=30, sticky="E")

    # Adding a task into the listbox
    def add_task(self):
        task = self.task_entry.get()   # getting the task from the new entry
        # Appending the new task, updating it in the listbox & deleting the task from the textbox
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tkr.END)
        else:
            messagebox.showwarning("Warning!!!", "Please enter a task!")  # shows warning when no task is entered in the text box

    # Updating the tasks in the listbox
    def update_task_listbox(self):
        self.task_listbox.delete(0, tkr.END)  # deletes the old task
        for task in self.tasks:
            self.task_listbox.insert(tkr.END, task) # updates the old task with a new task

    # Deleting a selected task from the listbox
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning!!!", "Please select a task to delete!")

    # Clearing all the tasks from the listbox
    def clear_all_tasks(self):
        confirm = messagebox.askyesno("Confirmation!", "Are you sure you wanna clear all tasks?")
        if confirm:
            self.tasks.clear()
            self.update_task_listbox()

if __name__ == "__main__":
    root = tkr.Tk()
    app = TodoListApp(root)
    root.mainloop()
