# testBeam2025
Programs for Raspberry Pi to control Velmex UniSlide motion system (via VXM Controller) and monitor MKS Mini Convectron 275 for Test Beam installation at JLab.

## Dependancies

-pySerial [https://pypi.org/project/pyserial/]
```
pip install pyserial
```

## Usage
Upon startup, to enable serial communication with the VXM Controller, run:
```
python vxmReady.py <optional parameter: speed (mm/sec)>
```
* When the VXM Controller is powered on, its current location becomes its zero position. It is recommended that the carriage is returned to the motorside endstop ("top") before cycling power to the VXM.
* A parameter may be passed to set the motor speed (in mm/sec). Allowed speeds must be greater than zero and no more than 6000 steps/sec (approx. 38 mm/sec).
  - If a speed outside this range is requested, the speed will be set to the nearest allowed extreme value.

To move the Velmex slider by a specific amount, run:
```
python module_control.py move <displacement in mm>
```
  - positive displacement: move the carriage downward
  - negative displacement: move the carriage upward


To home the Velmex slider to one of the limit switches:
```
python module_control.py limit <endstop>
```
  endstop options: "top" OR "bottom"


To montitor the MKS Mini Convectron 275:
```
python print_and_write.py
```
Be sure to edit line 53 with the approriate port for the Ardiuno. This program will create a file called "out.csv" and write the voltage and converted vacuum pressure sent by the Arduino to the file and the console. Finish collection and monitoring by pressing ctrl+c.
