from tkinter import *
from ttkthemes import ThemedStyle
import os
import json

class MainWindow:
    def __init__(self):
        # Initialize the main window
        self.root = Tk()
        self.root.minsize(600, 200)
        self.root.title("MCU and Sensor Selection")
        # Install and set the Arc theme (if desired)
        style = ThemedStyle(self.root)
        style.set_theme("arc")  # Set the theme to "arc"

        sensor_options = {}

        directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\..\\drivers\\mcus\\')
        print('Directory:', directory_path)
        # non recursive
        folders = [f.name for f in os.scandir(directory_path) if f.is_dir()]
        print(folders)
        for name in folders:
            f = open(directory_path + name + '\\' + name + '-config.json')
            print(f)
            data = json.load(f)
            sensor_options[name] = []
            for i in data['sensors']:
                sensor_options[name].append(i)
        
        f.close()

        mcu_list = []
        for mcu in sensor_options:
            mcu_list.append(mcu)
            
        # Function to update sensor options based on selected MCU
        def update_sensor_options():
            selected_mcu = mcu_var.get()
            sensor_options_list.delete(0, END)  # Clear previous options
            if mcu_list[selected_mcu] in mcu_list:
                for option in sensor_options[mcu_list[selected_mcu]]:
                    sensor_options_list.insert(END, option)
                    # Ensure listbox displays options even on initial selection

                sensor_options_list.yview(0)
                sensor_options_list.see(0)  # Scroll to the first item

        def create_file():
            # Before doing anything, disable all event handling to avoid glitches
            # sensor_options_list.config(state=DISABLED)  # Disallow selection
            # ...
            create_file_unsafe()
            # Re-enable event handling after the file is created

        def create_file_unsafe():
            filename = "my_file.txt"  # Replace with your desired filename logic
            folder_path = file_path.get()
            print('folder_path:', folder_path)
            try:
                file_path = folder_path + "\\" + filename
                print('file_path:', file_path)
                with open(file_path, "x") as file: # create only, fail if file exists
                    pass
                status_label.config(text="File created successfully in " + file_path + "!", fg="green")
            except FileNotFoundError:
                # Handle potential errors (e.g., invalid directory)
                status_label.config(text="Error creating file!", fg="red")

        # File path instruction label
        file_path_instruction = Label(self.root, text="Enter desired filepath (ex. C:/Carleton/BeavarByteBuilder):")
        file_path_instruction.pack(pady=5)

        # File path input
        text_value = StringVar()
        text_value.set("C:/Carleton/BeavarByteBuilder")
        file_path = Entry(self.root, width=50, textvariable=text_value)
        file_path.pack(pady=5)

        # Define variable for selected MCU (using IntVar)
        mcu_var = IntVar(self.root)  # Use IntVar for radio buttons
        # Set the initial selection to 0 (index of "Pi Pico" in the list)
        mcu_var.set(0)

        # Create MCU selection label
        mcu_label = Label(self.root, text="Select MCU:")
        mcu_label.pack(pady=5)

        # Create MCU radio buttons
        mcu_frame = Frame(self.root)
        mcu_frame.pack(pady=5)
        radio_button_count = 0  # Track radio button index
        for mcu, _ in sensor_options.items():  # Iterate over MCU names
            radiobutton = Radiobutton(mcu_frame, text=mcu, variable=mcu_var, value=radio_button_count, command=update_sensor_options)
            radiobutton.pack(side=LEFT, anchor=W)  # Pack radio buttons horizontally
            radio_button_count += 1  # Increment index for next radio button

        # Create sensor option label
        sensor_label = Label(self.root, text="Select Sensor Option:")
        sensor_label.pack(pady=10)

        # Create sensor option listbox
        sensor_options_list = Listbox(self.root, selectmode=MULTIPLE)
        sensor_options_list.config(state=NORMAL)  # Allow selection
        sensor_options_list.pack(pady=5)

        # Create a button to generate files
        generate_button = Button(self.root, text="Generate files", command=create_file)
        generate_button.pack(pady=10)

        # Create a status label to display messages after button click
        status_label = Label(self.root, text="")
        status_label.pack(pady=5)

        # Call update_sensor_options on startup to display initial options (fixed)
        update_sensor_options()

        # When "z" is pressed, FOR LOGGING ONLY
        def key_pressed(self):
            if (self.keysym == "z"):
              selected_text_list = [sensor_options_list.get(i) for i in sensor_options_list.curselection()]
              print(selected_text_list)
        self.root.bind("<Key>", key_pressed)

    def start(self):
        self.root.mainloop()