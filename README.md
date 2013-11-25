rasPyThermReader
================

A class to read temperature of multiple DS18B20+ temperature sensing on a Raspberry Pi

Hardware
--------

See (this tutorial on learn.adafruit.com)[http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing] to learn how to connect thermometers. 

With this script you may read multiple thermometers connected in parrallel.

Usage
-----

```python

import temperature #temperature.py must be in the same directory

t = temperature.TempReader() #use t = temperature.TempReader(True) if you want some debug information

#read temperature on thermometer 0 (the first thermometer)
c = t.thermometers[0].read_temp()

#read temperature of thermometer with serial number '28-0000046190ed'
try:
	d = t.getThermometer('28-0000046190ed').read_temp()
except temperature.ThermometerException as e:
	print(e) #this will print "The thermometer with id '28-0000046190ed' is not found." if this happen.

#temperatures are in ° Celsius
```
