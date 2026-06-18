from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.configure(bg="#EAF4FF")
root.state("zoomed")      # Start maximized
root.resizable(True, True)
# Center window
root.update_idletasks()
width = 500
height = 600
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")


def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, END)
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_listbox.insert(END, line.strip())
    except:
        pass
    update_count()

def renumber_tasks():
    tasks = task_listbox.get(0, END)

    task_listbox.delete(0, END)

    for i, task in enumerate(tasks, start=1):
        clean_task = task.split(". ", 1)[-1]
        task_listbox.insert(END, f"{i}. {clean_task}")   


def add_task():
    task = task_entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    task_number = task_listbox.size() + 1
    task_listbox.insert(END, f"{task_number}. {task}")

    task_entry.delete(0, END)

    update_count()
    save_tasks()


def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)

        renumber_tasks()
        update_count()
        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task first!")

def update_count():
    count_label.config(
        text=f"Tasks Remaining: {task_listbox.size()}"
    )


title = Label(
    root,
    text="My To-Do List",
    font=("Segoe UI", 22, "bold"),
    bg="#EAF4FF",
    fg="#0D47A1"
)
title.pack(pady=20)


task_entry = Entry(
    root,
    font=("Segoe UI", 14),
    width=28
)
task_entry.pack(pady=10, ipady=5)


add_btn = Button(
    root,
    text="Add Task",
    font=("Segoe UI", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=15,
    command=add_task
)
add_btn.pack(pady=10)


task_listbox = Listbox(
    root,
    font=("Segoe UI", 13),
    width=40,
    height=10,
    bg="white",
    selectbackground="#2196F3"
)
task_listbox.pack(pady=15, fill="both", expand=True)

delete_btn = Button(
    root,
    text="Delete Selected",
    font=("Segoe UI", 12, "bold"),
    bg="#FF5252",
    fg="white",
    width=15,
    command=delete_task
)
delete_btn.pack(pady=10)


count_label = Label(
    root,
    text="Tasks Remaining: 0",
    font=("Segoe UI", 12),
    bg="#EAF4FF",
    fg="#333333"
)
count_label.pack(pady=10)


load_tasks()

root.mainloop()