from tkinter import *
from ttkthemes import ThemedStyle

from scanMCUs import *
from sensorOptionList import *
from fileCreator import *

class MainWindow:
    def __init__(self):
        # INITIALIZATION: Create the main window
        self.root = Tk()
        self.root.minsize(600, 200)
        self.root.title("BeavarByte Builder")
        style = ThemedStyle(self.root)
        style.set_theme("arc")  # Set the theme to "arc"

        # CREATE COMPONENTS: Create the components for the main window
        sensor_options = {}
        scanFolders = ScanFolders()
        scanFolders.scanFolders(sensor_options)

        mcu_list = []
        sensorOptions = SensorOptions()
        sensorOptions.initialize_sensor_options(mcu_list, sensor_options)

        fileCreator = FileCreator()

        file_path_label = Label(self.root, text="Enter desired filepath (ex. C:/Carleton/BeavarByteBuilder):")
        file_path_label.pack(pady=5)

        file_path_input = StringVar()
        file_path_input.set("C:/Carleton/BeavarByteBuilder")
        file_path = Entry(self.root, width=50, textvariable=file_path_input)
        file_path.pack(pady=5)

        selected_MCU = IntVar(self.root)  # Use IntVar for radio buttons
        selected_MCU.set(0)

        mcu_selection_label = Label(self.root, text="Select MCU:")
        mcu_selection_label.pack(pady=5)

        mcu_frame = Frame(self.root)
        mcu_frame.pack(pady=5)
        radio_button_index = 0  # Radio button index
        for mcu, _ in sensor_options.items():  # Iterate over MCU names
            radiobutton = Radiobutton(mcu_frame, text=mcu, variable=selected_MCU, value=radio_button_index,
                command=lambda: sensorOptions.update_sensor_options(selected_MCU, sensor_options_listbox, mcu_list, sensor_options))
            radiobutton.pack(side=LEFT, anchor=W)  # Pack radio buttons horizontally
            radio_button_index += 1

        sensor_option_label = Label(self.root, text="Select Sensor Option:")
        sensor_option_label.pack(pady=10)

        sensor_options_listbox = Listbox(self.root, selectmode=MULTIPLE)
        sensor_options_listbox.config(state=NORMAL)  # Allow selection
        sensor_options_listbox.pack(pady=5)

        generate_button = Button(self.root, text="Generate files", 
            command=lambda: fileCreator.create_file(file_path, status_label))
        generate_button.pack(pady=5)

        status_label = Label(self.root, text="")
        status_label.pack(pady=5)

        # STARTUP: Call on startup to display initial options
        sensorOptions.update_sensor_options(selected_MCU, sensor_options_listbox, mcu_list, sensor_options)

    def start(self):
        self.root.mainloop()