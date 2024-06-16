# Sensor configuration folder

Folder names: Must be all lowercase, spaces denoted by "-" character. 
Configuration file names: Must follow <folder-name>-config.json

# Sensor configuration file
|Key Identfier|Type|Description|
|-|-|-|
|mcus| List of objects | List of microcontroller that are compatible.
|name| String | Name of microcontroller|
|specialized_pinouts| List of objects pinouts that can be configured.  | specialized_pinouts is used for pins that have certain designated connections to the mcu. For example, not all pins are SPI, hence sensors using SPI must list out which mcu pins can be used. These pinouts have higher priority than the normal_pinouts when the code gen selects pins.
|normal_pinouts| Object| Any pins that have multiple possible connections to the MCU and don't require specialized connection are designated as normal pinouts. For example, a sensor using GPIO or ADC, may have a dozen possible pins, the code gen tool will assign any remaining mcus pins to these sensor pins.
|driver_includes| List of string| List of libraries that need to be included for the sensor|
|init_driver_function| String| Name of initialization function that should be called.
