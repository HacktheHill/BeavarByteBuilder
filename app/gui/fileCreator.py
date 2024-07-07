from tkinter import *

class FileCreator:
    def create_file(self, file_path, status_label):
        filename = "my_file.txt"  # Replace with your desired filename logic
        folder_path = file_path.get()
        try:
            file_path = folder_path + "/" + filename
            print('file_path:', file_path)
            with open(file_path, "x") as file: # create only, fail if file exists
                pass
            status_label.config(text=f"File created successfully: {file_path}!", fg="green")
        except Exception as e:
            # Handle potential errors (e.g., invalid directory)
            status_label.config(text=f"ERROR: {e}!", fg="red")
            pass