import tkinter as tk
from tkinter import filedialog

# ---------------- Browse Folder Function ----------------

def browse_folder():
    folder_path = filedialog.askdirectory()

    if folder_path:
        folder_path_var.set(folder_path)


# Create main application window
app = tk.Tk()

# Set window title
app.title("Smart File Organizer")

# Set window size
app.geometry("700x500")


# Application title
title_label = tk.Label(
    app,
    text="Smart File Organizer",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=30)


# Subtitle
subtitle_label = tk.Label(
    app,
    text="Organize your files automatically",
    font=("Arial", 12)
)

# ---------------- Folder Selection ----------------

folder_label = tk.Label(
    app,
    text="Select Folder",
    font=("Arial", 12, "bold")
)

subtitle_label.pack()


# Variable to store selected folder path
folder_path_var = tk.StringVar()


# Frame to keep input and button on same row
folder_frame = tk.Frame(app)

folder_frame.pack(pady=10)


# Folder path input
folder_entry = tk.Entry(
    folder_frame,
    textvariable=folder_path_var,
    width=50
)

folder_entry.pack(side="left", padx=(0, 10))


# Browse button
browse_button = tk.Button(
    folder_frame,
    text="Browse",
    command=browse_folder
)

browse_button.pack(side="left")



# Start the GUI application
app.mainloop()