# File Classifier GUI

This is a Python-based GUI application that allows you to automatically organize files in a selected directory into folders based on their file types. The application uses the `tkinter` library to create a user-friendly interface.

## Features

- **File Type Classification:** The application identifies and moves files into folders based on their extensions such as `.pdf`, `.txt`, `.jpeg`, `.jpg`, `.png`, `.exe`, `.xlsx`, and `.zip`.
- **User-Friendly Interface:** The GUI allows users to enter the folder path manually or browse to select a folder.
- **Automatic Folder Creation:** The application creates folders for each file type if they don't already exist in the selected directory.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)

## Installation

1. **Clone the repository** (if applicable) or download the script files.
   
2. **Navigate to the project directory**:
   ```bash
   cd /path/to/project

3. Run the script
   python gui.py

 ## Example
 
Here’s what happens when you classify files in a directory:

Files like document.pdf, image.jpeg, and spreadsheet.xlsx will be moved into pdf, jpeg, and xlsx folders respectively within the selected directory.

## Notes

The application does not delete or overwrite existing files. If a file with the same name already exists in the destination folder, the operation will be skipped.
The GUI may not display all file types; only the specified extensions are supported in this version.

## License

This project is licensed under the MIT License.

## Author

Divyanshi Maurya (12219959)
