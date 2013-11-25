rasPyThermReader
================

A class to read temperature of multiple DS18B20+ temperature sensing on a Raspberry Pi

Usage
-----

```python

import temperature

t = temperature.TempReader() #use t = temperature.TempReader(True) if you want some debug information

#read temperature on thermometer 0 (the first thermometer)
c = t.thermometers[0].read_temp()

#temperature is in ° Celsius
