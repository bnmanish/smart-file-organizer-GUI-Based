import tkinter as tk
from tkinter import filedialog
from pathlib import Path

from function import get_category


# ---------------- Browse Folder ----------------

def browse_folder():
    folder_path = filedialog.askdirectory()

    if folder_path:
        folder_path_var.set(folder_path)


# ---------------- Preview Files ----------------

def preview_files():
    selected_folder = folder_path_var.get()

    if not selected_folder:
        status_label.config(text="Please select a folder first.")
        return

    counts = {
        "PDF": 0,
        "Image": 0,
        "Video": 0,
        "Document": 0,
        "Other": 0
    }

    total_files = 0

    try:
        for file in Path(selected_folder).iterdir():

            if not file.is_file():
                continue

            category = get_category(file.suffix.lower())

            counts[category] += 1
            total_files += 1

    except OSError as error:
        status_label.config(
            text=f"Unable to read folder: {error}"
        )
        return

    # Clear previous preview
    preview_text.delete("1.0", tk.END)

    preview_text.insert(
        tk.END,
        f"Total Files : {total_files}\n\n"
    )

    for category, count in counts.items():
        preview_text.insert(
            tk.END,
            f"{category:<10}: {count}\n"
        )

    status_label.config(text="Preview generated successfully.")


# ---------------- Main Window ----------------

app = tk.Tk()

app.title("Smart File Organizer")
app.geometry("700x500")


# ---------------- Title ----------------

title_label = tk.Label(
    app,
    text="Smart File Organizer",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(30, 10))


# ---------------- Subtitle ----------------

subtitle_label = tk.Label(
    app,
    text="Organize your files automatically",
    font=("Arial", 12)
)

subtitle_label.pack(pady=(0, 25))


# ---------------- Folder Selection ----------------

folder_label = tk.Label(
    app,
    text="Select Folder",
    font=("Arial", 12, "bold")
)

folder_label.pack()


folder_path_var = tk.StringVar()


folder_frame = tk.Frame(app)

folder_frame.pack(pady=10)


folder_entry = tk.Entry(
    folder_frame,
    textvariable=folder_path_var,
    width=50
)

folder_entry.pack(side="left", padx=(0, 10))


browse_button = tk.Button(
    folder_frame,
    text="Browse",
    command=browse_folder
)

browse_button.pack(side="left")


# ---------------- Preview Button ----------------

preview_button = tk.Button(
    app,
    text="Preview Files",
    command=preview_files
)

preview_button.pack(pady=15)


# ---------------- Preview Result ----------------

preview_text = tk.Text(
    app,
    width=50,
    height=10
)

preview_text.pack(pady=10)


# ---------------- Status ----------------

status_label = tk.Label(
    app,
    text="Ready",
    font=("Arial", 10)
)

status_label.pack(pady=5)


# ---------------- Start Application ----------------

app.mainloop()