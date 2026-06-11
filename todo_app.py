import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
entry = tk.Entry(root,width=20)
entry.pack(pady=10)
listbox = tk.Listbox(root,width = 30,height = 8)
listbox.pack(pady=10)
def add_task():
    task = entry.get()
    listbox.insert(tk.END,task)
    entry.delete(0,tk.END)
tk.Label(root,text="Welcome",font=("Arial",18,"bold"),fg ="black",bg="white").pack()
tk.Button(root,text="Add Task",command=add_task).pack(pady=10)
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
tk.Button(root,text="Delete Task",command=delete_task).pack()
def clear_all():
    listbox.delete(0,tk.END)
tk.Button(root,text="Clear all",command=clear_all).pack()
root.mainloop()