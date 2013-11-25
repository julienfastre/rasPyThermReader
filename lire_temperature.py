
import temperature
import time

t = temperature.TempReader(True)

while True:
	c = t.thermometers[0].read_temp()
	print("Thermometer 0 " + str(c) )
	c1 = t.thermometers[1].read_temp()
	print("Thermometer 1 " + str(c1) )
	
	time.sleep(1)