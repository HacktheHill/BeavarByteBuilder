from tkinter import *
from git import Repo  # pip install gitpython

class DownloadLibrary:
    def fetchFromGithub(self, folder: StringVar, status_label_download: Label):
        folder_path = folder.get()
        print('folder_path:', folder_path)
        # TODO
        try:
            git_url = "https://github.com/stm32duino/VL53L5CX"
            Repo.clone_from(git_url, folder_path)
            status_label_download.config(text=f"Repo cloned successfully: {folder_path}!", fg="green")
        except Exception as e:
            status_label_download.config(text=f"ERROR: {e}!", fg="red")
            pass