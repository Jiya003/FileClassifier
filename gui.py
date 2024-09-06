import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

def classify_files():
    path = path_entry.get()
    if not os.path.exists(path):
        messagebox.showerror("Error", "Invalid path!")
        return

    dir_list = os.listdir(path)
    files = [f for f in dir_list if os.path.isfile(os.path.join(path, f))]

    file_types = {
        'pdf': [f for f in files if f.endswith('.pdf')],
        'txt': [f for f in files if f.endswith('.txt')],
        'jpeg': [f for f in files if f.endswith('.jpeg')],
        'jpg': [f for f in files if f.endswith('.jpg')],
        'png': [f for f in files if f.endswith('.png')],
        'exe': [f for f in files if f.endswith('.exe')],
        'xlsx': [f for f in files if f.endswith('.xlsx')],
        'zip': [f for f in files if f.endswith('.zip')],
    }

    for folder, file_list in file_types.items():
        if not file_list:
            continue
        
        folder_path = os.path.join(path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file_name in file_list:
            shutil.move(os.path.join(path, file_name), os.path.join(folder_path, file_name))

    messagebox.showinfo("Success", "Files have been classified!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)

# GUI Setup
root = tk.Tk()
root.title("File Classifier")
root.geometry("500x200")

tk.Label(root, text="Enter or Browse Folder Path:").pack(pady=10)
path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(root, text="Classify Files", command=classify_files).pack(pady=20)

root.mainloop()
