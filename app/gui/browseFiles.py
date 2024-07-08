from tkinter import *
from tkinter.filedialog import askdirectory

class BrowseFiles:
    def browse_file(self, file_var: StringVar):
        file_path = askdirectory()
        print(file_path)
        file_var.set(file_path)