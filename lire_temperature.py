
import temperature
import time

t = temperature.TempReader(True)

try:
	c3 = t.getThermometer('zero')
except temperature.ThermometerException as e:
	print(e)



while True:
	c = t.thermometers[0].read_temp()
	print("Thermometer 0 " + str(c) )
	c1 = t.thermometers[1].read_temp()
	print("Thermometer 1 " + str(c1) )

	d = t.getThermometer('28-0000046190ed').read_temp()
	print("Thermometer 46190ed is " + str(d) + "°C")
	
	time.sleep(1)
