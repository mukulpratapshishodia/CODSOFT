import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(self.root, text="Mark Completed", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        self.view_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index] = f"✓ {self.tasks[index]}"
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, self.tasks[index])
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def view_tasks(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Tasks")

        if self.tasks:
            for task in self.tasks:
                label = tk.Label(view_window, text=task)
                label.pack(padx=10, pady=5)
        else:
            label = tk.Label(view_window, text="No tasks yet!")
            label.pack(padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
