from tkinter import *

class ValidatePinout:
    def validatePinout(self, folder: StringVar, status_label_validate: Label):
        folder_path = folder.get()
        print('folder_path:', folder_path)
        # TODO
        try:
            status_label_validate.config(text=f"Pinout is valid: {folder_path}!", fg="green")
        except InvalidPinoutError as e:
            status_label_validate.config(text=f"{e}! Check the log file for details: {folder_path}", fg="red")
            pass
        except Exception as e:
            status_label_validate.config(text=f"ERROR: {e}!", fg="red")
            pass