from tkinter import *
from ttkthemes import ThemedStyle

# Define sensor options for each MCU
sensor_options = {
    "Pi Pico": ["E paper display", "Transparent OLED", "8x8 ToF Sensor", "JoyStick", "LCD", "Servo", "Seven Seg", "Temperature sensor DHT 11", "Ultrasonic sensor", "Photoresistor", "Button", "Myoware sensor"],
    "Arduino Nano 33 BLE": ["E paper display", "Transparent OLED", "8x8 ToF Sensor", "JoyStick", "LCD", "Servo", "Seven Seg", "Temperature sensor DHT 11", "Ultrasonic sensor", "Photoresistor", "Button", "Myoware sensor"],
    "Adafruit Atmega32U4": ["JoyStick", "LCD", "Servo", "Seven Seg", "Temperature sensor DHT 11", "Ultrasonic sensor", "Photoresistor", "Button", "Myoware sensor", "Keyboard Emulation"],
    "SeeedStudio mmWave Radar Kit": [],  # No sensor options for mmWave Radar
}

sensor_pins = {
"E paper display": [],
"Transparent OLED": [3, 5, 11, 12],
"8x8 ToF Sensor": ["A4", "A5"],
"JoyStick": [0, 1],
"LCD": [2, 4, 6, 7, 8, 9, 10],
"Servo": [5, 6, 9, 10],
"Seven Seg": [2, 3, 4, 5, 8, 9, 10],
"Temperature sensor DHT 11": [2],
"Ultrasonic sensor": [2, 6],
"Photoresistor": ["A0"],
"Button": [7],
"Myoware sensor": [],  
"Keyboard Emulation": []  
}

digital_pins = [True] * 14
analog_pins = [True] * 6

mcu_list = []
for mcu in sensor_options:
    mcu_list.append(mcu)
    
# Function to update sensor options based on selected MCU
def update_sensor_options():
    selected_mcu = mcu_var.get()
    sensor_option_var.set("")  # Clear previous selection
    sensor_options_list.config(state=NORMAL)  # Allow selection
    sensor_options_list.delete(0, END)  # Clear previous options
    print(mcu_list[selected_mcu])
    print(mcu_list)
    if mcu_list[selected_mcu] in mcu_list:
        for option in sensor_options[mcu_list[selected_mcu]]:
            sensor_options_list.insert(END, option)
        # Ensure listbox displays options even on initial selection

        sensor_options_list.yview(0)
        sensor_options_list.see(0)  # Scroll to the first item
        # sensor_options_list.config(state=DISABLED)  # Disallow selection

def update_available_sensor_options():
    selected_mcu = mcu_var.get()
    sensor_option_var.set("")  # Clear previous selection
    sensor_options_list.config(state=NORMAL)  # Allow selection
    sensor_options_list.delete(0, END)  # Clear previous options
    print(mcu_list[selected_mcu])
    print(mcu_list)
    if mcu_list[selected_mcu] in mcu_list:
        for option in sensor_options[mcu_list[selected_mcu]]:
            sensor_options_list.insert(END, option)
        # Ensure listbox displays options even on initial selection

        sensor_options_list.yview(0)
        sensor_options_list.see(0)  # Scroll to the first item
        sensor_options_list.config(state=DISABLED)  # Disallow selection

# Initialize the main window
root = Tk()
root.title("MCU and Sensor Selection")

# Install and set the Arc theme (if desired)
style = ThemedStyle(root)
style.set_theme("arc")  # Set the theme to "arc"

# Define variable for selected MCU (using IntVar)
mcu_var = IntVar(root)  # Use IntVar for radio buttons
# Set the initial selection to 0 (index of "Pi Pico" in the list)
mcu_var.set(0)

# Create MCU selection label
mcu_label = Label(root, text="Select MCU:")
mcu_label.pack(pady=5)

# Create MCU radio buttons
mcu_frame = Frame(root)
mcu_frame.pack()
radio_button_count = 0  # Track radio button index
for mcu, _ in sensor_options.items():  # Iterate over MCU names
    radiobutton = Radiobutton(mcu_frame, text=mcu, variable=mcu_var, value=radio_button_count, command=update_sensor_options)
    radiobutton.pack(side=LEFT, anchor=W)  # Pack radio buttons horizontally
    radio_button_count += 1  # Increment index for next radio button

# Define variable for selected sensor option (using StringVar)
sensor_option_var = StringVar(root)

# Create sensor option label
sensor_label = Label(root, text="Select Sensor Option:")
sensor_label.pack(pady=10)

# Create sensor option listbox
sensor_options_list = Listbox(root, listvariable=sensor_option_var, selectmode=MULTIPLE, command=update_available_sensor_options)
sensor_options_list.pack()

# Function to create an empty file
def create_empty_file():
    # Get the filename from a user input or define a default filename here
    filename = "my_file.txt"  # Replace with your desired filename logic
    try:
        # Open the file in write mode (creates a new file if it doesn't exist)
        with open(filename, "w") as file:
            pass  # Empty pass statement to create the empty file
        # Show success message
        status_label.config(text="Empty file created successfully!", fg="green")
    except FileNotFoundError:
        # Handle potential errors (e.g., invalid directory)
        status_label.config(text="Error creating file!", fg="red")

# Create a button with the "Generate" label and call the create_empty_file function on click
generate_button = Button(root, text="Generate", command=create_empty_file)
generate_button.pack(pady=10)

# Create a status label to display messages after button click
status_label = Label(root, text="")
status_label.pack()

# Call update_sensor_options on startup to display initial options (fixed)
update_sensor_options()

# Run the main event loop
root.mainloop()