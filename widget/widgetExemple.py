import tkinter as tk
from tkinter import ttk

root = tk.Tk()

container = ttk.Frame(root)

first_label = ttk.Label(container, text="First name")
last_label = ttk.Label(container, text="Last name")

first_entry = ttk.Entry(container)
last_entry = ttk.Entry(container)

quit_button = ttk.Button(container, text="Quit")
show_button = ttk.Button(container, text="show")


container.grid(column=0, row=0)
first_label.grid(column=0, row=0)
first_entry.grid(column=1, row=0)
last_label.grid(column=0, row=1)
last_entry.grid(column=1, row=1)
quit_button.grid(column=0, row=2)
show_button.grid(column=1, row=2)

root.mainloop()
