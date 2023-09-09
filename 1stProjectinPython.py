# Task 1:-
# TO-DO LIST APPLICATION:-
# Our aim is add the features like:- 1. Add Items , 2. Delete Items, 3.Clear All Items
# Program Implementation:-
# we shall use  a GUI(i.e tkinter) :-

import tkinter as tk
from tkinter import messagebox

# if-else syntax would be used below:-

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a item to add it in your todo-list.")

# Exception Handling  syntax would be introduced below:-
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a Item which you want to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("TO-DO LIST APPLICATION")

# Create and configure the task entry widget
task_entry = tk.Entry(root, width=45)
task_entry.pack(pady=29)

# Create buttons for adding, deleting, and clearing tasks
add_button = tk.Button(root, text="Add Items", command=add_task)# By this button, we can add the string items
delete_button = tk.Button(root, text="Delete Items", command=delete_task)# By this button, we can delete string items
clear_button = tk.Button(root, text="Clear All Items", command=clear_tasks)# By this button, we can delete all the string items

add_button.pack()
delete_button.pack()
clear_button.pack()

# Create and configure the task listbox
task_listbox = tk.Listbox(root, width=60, height=13)
task_listbox.pack()

root.mainloop()
