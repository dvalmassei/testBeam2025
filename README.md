# testBeam2025
Programs for Raspberry Pi to control Velmex motion system and monitor MKS Mini Convectron 275 for Test Beam installation at JLab.

## Dependancies

-pySerial [https://pypi.org/project/pyserial/]
```
pip install pyserial
```

## Usage

To move the Velmex slider by a specific amount, run:
```
python velmex_move.py <distance in mm>
```

To home the Velmex slider to one of the endstops:
```
python velmex_home.py <0>
```

To montitor the MKS Mini Convectron 275:
```
python print_and_write.py
```
Be sure to edit line 53 with the approriate port for the Ardiuno. This program will will create a file called "out.csv" and write the voltage and converted vacuum pressure sent by the Arduino to the file and the console.
