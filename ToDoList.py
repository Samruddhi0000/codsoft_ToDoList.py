import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.dark_mode = False  # Start in light mode
        self.tasks = []

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12), width=40, height=10)
        self.task_listbox.pack(pady=20)

        # Entry for new task
        self.task_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=5)

        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Buttons
        self.buttons = []
        btn_add = tk.Button(button_frame, text="Add Task", command=self.add_task)
        btn_edit = tk.Button(button_frame, text="Edit Task", command=self.edit_task)
        btn_delete = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        btn_save = tk.Button(button_frame, text="Save Tasks", command=self.save_tasks)
        btn_theme = tk.Button(self.root, text="Toggle Theme", command=self.toggle_theme)

        # Place buttons in layout
        btn_add.grid(row=0, column=0, padx=5)
        btn_edit.grid(row=0, column=1, padx=5)
        btn_delete.grid(row=0, column=2, padx=5)
        btn_save.grid(row=0, column=3, padx=5)
        btn_theme.pack(pady=10)

        # Store buttons in list for theme styling
        self.buttons.extend([btn_add, btn_edit, btn_delete, btn_save, btn_theme])

        self.load_tasks()
        self.apply_theme()  # Set initial theme

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def edit_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Edit Task", "Update the selected task:", initialvalue=self.tasks[selected])
            if new_task:
                self.tasks[selected] = new_task
                self.task_listbox.delete(selected)
                self.task_listbox.insert(selected, new_task)
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
            self.tasks.pop(selected)
        except IndexError:
            messagebox.showwarning("Select Task", "Please select a task to delete.")

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                for line in f:
                    task = line.strip()
                    if task:
                        self.tasks.append(task)
                        self.task_listbox.insert(tk.END, task)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            bg_color = "#2e2e2e"
            fg_color = "#ffffff"
            entry_bg = "#3a3a3a"
        else:
            bg_color = "#f0f0f0"
            fg_color = "#000000"
            entry_bg = "#ffffff"

        self.root.config(bg=bg_color)
        self.task_listbox.config(bg=entry_bg, fg=fg_color)
        self.task_entry.config(bg=entry_bg, fg=fg_color, insertbackground=fg_color)

        for button in self.buttons:
            button.config(
                bg="#007bff", fg="white",
                activebackground="#0056b3", activeforeground="white"
            )

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
