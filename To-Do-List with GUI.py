import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")

        self.tasks = []

        self.intro_label = tk.Label(master, text="Welcome to Task Manager", font=("Helvetica", 16))
        self.intro_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=1, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=40, height=10)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, padx=5, pady=5)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=3, column=1, padx=5, pady=5)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            task = Task(task_description)
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task.description)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.completed = True
            self.task_listbox.itemconfig(selected_index, {'bg': 'light green', 'fg': 'gray'})
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
