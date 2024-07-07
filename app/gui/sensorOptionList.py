from tkinter import *

class SensorOptions:
    def initialize_sensor_options(self, mcu_list, sensor_options):
        for mcu in sensor_options:
            mcu_list.append(mcu)
            
    # Function to update sensor options based on selected MCU
    def update_sensor_options(self, selected_MCU, sensor_options_listbox, mcu_list, sensor_options):
        selected_mcu = selected_MCU.get()
        sensor_options_listbox.delete(0, END)  # Clear previous options
        if mcu_list[selected_mcu] in mcu_list:
            for option in sensor_options[mcu_list[selected_mcu]]:
                sensor_options_listbox.insert(END, option)
                # Ensure listbox displays options even on initial selection

            sensor_options_listbox.yview(0)
            sensor_options_listbox.see(0)  # Scroll to the first item