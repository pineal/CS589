import pyupm_gas as TP401
from AbstractSensor import AbstractSensor
from collections import deque

class AirSensor(AbstractSensor):

	def __init__(self,pin,precision):
		self.airSensor = TP401.TP401(pin)
		self.precision = precision
		self.readings=deque(10*[0],10)

	def readData(self):

		self.readings.append(self.airSensor.getPPM())
		self.data = sum(self.readings)/float(10)

		return round(self.data, self.precision)