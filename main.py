import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "task.json"

# ---------- Functions ----------
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                tasks = json.load(f)
                for task in tasks:
                    listbox.insert(tk.END, task)
            except json.JSONDecodeError:
                pass  # empty file case


def save_tasks():
    tasks = list(listbox.get(0, tk.END))
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()


def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")


# ---------- GUI ----------
root = tk.Tk()
root.title("TO-DO LIST")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=16, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=16, command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
listbox.pack(pady=10)

load_tasks()

root.mainloop()
