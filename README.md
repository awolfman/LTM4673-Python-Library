# LTM4673 Python Library

## Introduction

The LTM4673 Python Library provides a user-friendly interface for interacting for configure the LTM4673 over I2C. The library allows for easy configuration and data acquisition, supporting various settings for voltage range, etc

If you have any questions, please contact the Repo-Owner.

## Getting Started

Follow these steps to get the code up and running on your system:

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ltm4673-python-library.git
   cd ltm4673-python-library
   ```

2. **Install the required Python packages:**
   ```bash
   pip install smbus
   ```
   
### Software Dependencies

- Python 3.x
- smbus library for I2C communication

## Usage Example

Here's an example of how to use the library:

```python
from ltm4673 import LTC2975

# Initialize the sensor
DEFAULT_BUS = 1
I2CBASEADDR = 0x5b

sensor = LTC2975(bus_num=DEFAULT_BUS, addr=I2CBASEADDR)

# Read values

print (f"Device ID: {hex(sensor.mfr_special_id())}")
print (f"Customer Codes: {hex(sensor.mfr_special_lot())}")
print ("Vin = {:.2f} V".format(sensor.read_vin() ))
print ("Iin = {:.2f} A".format(sensor.read_iin() ))
print (f"Status Input: {hex(sensor.status_input())}")

# Write values

# Disable write protection
sensor.write_protect(0x00) 

# Set the input voltage turn-on threshold
sensor.vin_on(0xD200)

# Servo target. Nominal DC/DC converteroutput voltage setpoint 1.2V
sensor.vout_command(1.2)
```
### API Overview

#### Initialization

```python
sensor = LTC2975(bus_num=1, addr=0x40)
```
- `bus_num`: The I2C bus number (default is 1).
- `addr`: The I2C address of the LTM4673 (default is 0x5b).

#### Reading Values

```python
vin_voltage = sensor.read_vin()
input_current = sensor.read_iin()
```
### Device Information

To get the device ID:

```python
device_id = sensor.mfr_special_id()
print(f"Device ID: {device_id}")
```
## To Do's:
- [ ] Implement block reading of registers
- [ ] Implement reading/writing of CF registers
