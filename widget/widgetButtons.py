import tkinter as tk
from tkinter import ttk

def quit_app():
    root.quit()

def show_widget():
    # Get the text from the entries
    first_name = first_entry.get()
    last_name = last_entry.get()
    
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Add a label to the new window displaying the entered names
    label = ttk.Label(new_window, text=f"First Name: {first_name}\nLast Name: {last_name}")
    label.pack(padx=20, pady=20)

# Initialize the main window
root = tk.Tk()

container = ttk.Frame(root)

# Create the labels and entries
first_label = ttk.Label(container, text="First name")
last_label = ttk.Label(container, text="Last name")

first_entry = ttk.Entry(container)
last_entry = ttk.Entry(container)

# Create the buttons and assign the functions
quit_button = ttk.Button(container, text="Quit", command=quit_app)
show_button = ttk.Button(container, text="Show", command=show_widget)

# Layout the widgets in the grid
container.grid(column=0, row=0)
first_label.grid(column=0, row=0)
first_entry.grid(column=1, row=0)
last_label.grid(column=0, row=1)
last_entry.grid(column=1, row=1)
quit_button.grid(column=0, row=2)
show_button.grid(column=1, row=2)

# Start the main event loop
root.mainloop()
