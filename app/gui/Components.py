from tkinter import *
from ttkthemes import ThemedStyle

from scanMCUs import *
from sensorOptionList import *
from fileCreator import *
from browseFiles import *
from downloadLibrary import *
from validatePinout import *
from predictPath import *

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
        browseFiles = BrowseFiles()
        downloadLibrary = DownloadLibrary()
        validatePinout = ValidatePinout()
        predictPath = PredictPath()

        Label(self.root, text="Enter desired filepath (ex. C:/Users/liamp/OneDrive/Documents/Arduino/libraries):").pack(pady=5)
        file_download_var = StringVar()
        status_label_prediction = Label(self.root, text="")
        hardware = "VL53L5CX"
        file_download_var.set(predictPath.getArduinoPath(status_label_prediction, hardware))  # Predict the Arduino path
        Entry(self.root, width=50, textvariable=file_download_var).pack(pady=5)
        status_label_prediction.pack(pady=5)
        Button(self.root, text="Browse Files", 
            command=lambda: browseFiles.browse_file(file_download_var)).pack(pady=5)
        status_label_download = Label(self.root, text="")
        Button(self.root, text="Download Library", 
            command=lambda: downloadLibrary.fetchFromGithub(file_download_var, status_label_download)).pack(pady=5)
        status_label_download.pack(pady=5)

        Label(self.root, text="Enter desired filepath (ex. C:/Carleton/LogFiles):").pack(pady=5)
        file_validate_var = StringVar()
        file_validate_var.set("LogFiles")
        Entry(self.root, width=50, textvariable=file_validate_var).pack(pady=5)
        Button(self.root, text="Browse Files", 
            command=lambda: browseFiles.browse_file(file_validate_var)).pack(pady=5)
        status_label_validate = Label(self.root, text="")
        Button(self.root, text="Validate Pinout", 
            command=lambda: validatePinout.validatePinout(file_validate_var, status_label_validate)).pack(pady=5)
        status_label_validate.pack(pady=5)

        selected_MCU = IntVar(self.root)  # Use IntVar for radio buttons
        selected_MCU.set(0)

        Label(self.root, text="Select MCU:").pack(pady=5)

        mcu_frame = Frame(self.root)
        mcu_frame.pack(pady=5)
        radio_button_index = 0  # Radio button index
        for mcu, _ in sensor_options.items():  # Iterate over MCU names
            radiobutton = Radiobutton(mcu_frame, text=mcu, variable=selected_MCU, value=radio_button_index,
                command=lambda: sensorOptions.update_sensor_options(selected_MCU, sensor_options_listbox, mcu_list, sensor_options))
            radiobutton.pack(side=LEFT, anchor=W)  # Pack radio buttons horizontally
            radio_button_index += 1

        Label(self.root, text="Select Sensor Option:").pack(pady=10)

        sensor_options_listbox = Listbox(self.root, selectmode=MULTIPLE)
        sensor_options_listbox.config(state=NORMAL)  # Allow selection
        sensor_options_listbox.pack(pady=5)

        Label(self.root, text="Enter desired filepath (ex. Downloads):").pack(pady=5)
        file_gen_var = StringVar()
        file_gen_var.set("Downloads")
        Entry(self.root, width=50, textvariable=file_gen_var).pack(pady=5)
        Button(self.root, text="Browse Files", 
            command=lambda: browseFiles.browse_file(file_gen_var)).pack(pady=5)
        status_label_generate = Label(self.root, text="")
        Button(self.root, text="Generate files", 
            command=lambda: fileCreator.create_file(file_gen_var, status_label_generate)).pack(pady=5)
        status_label_generate.pack(pady=5)

        # STARTUP: Call on startup to display initial options
        sensorOptions.update_sensor_options(selected_MCU, sensor_options_listbox, mcu_list, sensor_options)

    def start(self):
        self.root.mainloop()