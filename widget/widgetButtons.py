import tkinter as tk
from tkinter import ttk

# Constants for sizes
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
PADDING = 10

def quit_app():
    root.quit()

def show_widget():
    # Get the text from the entries
    first_name = first_entry.get()
    last_name = last_entry.get()
    
    # Clear the existing widgets in the container
    for widget in container.winfo_children():
        widget.destroy()
    
    # Add a label displaying the entered names
    label = ttk.Label(container, text=f"First Name: {first_name}\nLast Name: {last_name}")
    label.grid(column=0, row=0, columnspan=2, padx=PADDING, pady=PADDING)
    
    # Recreate the Quit button to allow exiting the app
    quit_button = ttk.Button(container, text="Quit", command=quit_app)
    quit_button.grid(column=0, row=1, columnspan=2, padx=PADDING, pady=PADDING)

# Initialize the main window
root = tk.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

container = ttk.Frame(root, padding=PADDING)

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
