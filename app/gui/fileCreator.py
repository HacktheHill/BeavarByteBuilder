from tkinter import *

class FileCreator:
    def create_file(self, folder: StringVar, status_label_generate: Label):
        folder_path = folder.get()
        print('folder_path:', folder_path)
        filename = "my_file.txt"  # Replace with your desired filename logic
        try:
            file_path = folder_path + "/" + filename
            print('file_path:', file_path)
            with open(file_path, "x") as file: # create only, fail if file exists
                pass
            status_label_generate.config(text=f"File created successfully: {file_path}!", fg="green")
        except Exception as e:
            status_label_generate.config(text=f"ERROR: {e}!", fg="red")
            pass