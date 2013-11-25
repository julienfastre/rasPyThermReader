import os
import glob
import time

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')



class TempReader:

	base_dir = '/sys/bus/w1/devices/'
	base_file = '/w1_slave'
	folder_prefix = '28*'


	thermometers = []

	def __init__(self, debug = False):
		device_folders = glob.glob(self.base_dir + self.folder_prefix)
		self._debug = debug

		for folder in device_folders:
			t = Thermometer(folder, self.base_file)
			self.thermometers.append(t)

		if (self._debug):
			print("there are " + str(len(self.thermometers)) + " theremometers connected")



class Thermometer:

	_device_file = ''

	def __init__(self, folder, base):
		self._device_file = folder + base

	def read_temp_raw(self):
		f = open(self._device_file, 'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.read_temp_raw()
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			return temp_c






