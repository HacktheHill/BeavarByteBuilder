from tkinter import *
import json

class ValidatePinout:
    def _assign_mcu_pinouts(mcu_data):
        mcu = mcu_data['normal_pinouts']
        pinout_assignments = {}
        used_pinouts = set()

        # Create a stack for backtracking
        stack = list(mcu.items())
        while stack:
            pinout, locations = stack[-1]

            # Try to assign a pinout
            for location in locations:
                if location not in used_pinouts:
                    pinout_assignments[pinout] = location
                    used_pinouts.add(location)
                    break
            else:
                # No pinout could be assigned, backtrack
                if pinout in pinout_assignments:
                    used_pinouts.remove(pinout_assignments[pinout])
                    del pinout_assignments[pinout]
                stack.pop()
                continue

            # Check if all pinouts have been assigned
            if len(pinout_assignments) == len(mcu):
                return pinout_assignments

            # Move on to the next pinout
            stack.append(list(mcu.items())[len(pinout_assignments)])

        return None

    def validatePinout(self, folder: StringVar, status_label_validate: Label):
        folder_path = folder.get()
        print('folder_path:', folder_path)
        filename = "BeavarBytes_LogFile.txt"
        # TODO

        try:
            # Load MCU data from a JSON file
            file_path = folder_path + "/" + filename
            print('file_path:', file_path)
            with open('mcu_data.json', 'r') as f:
                mcu_data = json.load(f)

            pinout_assignments = ValidatePinout._assign_mcu_pinouts(mcu_data['mcus'][0])

            if pinout_assignments is None:
                print("No valid pinout assignments found.")
                status_label_validate.config(text=f"{e}! Check the log file for details: {folder_path}", fg="red")
            else:
                print("Pinout assignments:")
                for pinout, location in pinout_assignments.items():
                    print(f"{pinout}: {location}")
                status_label_validate.config(text=f"Pinout is valid: {folder_path}!", fg="green")

        except Exception as e:
            status_label_validate.config(text=f"ERROR: {e}!", fg="red")
            pass