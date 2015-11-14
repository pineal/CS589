import pyupm_grove as grove
from AbstractSensor import AbstractSensor

class TemperatureSensor(AbstractSensor):

	def __init__(self,pin,unit):
		self.tempSensor = grove.GroveTemp(pin)
		self.unit = unit
		pass

	def readData(self):
		self.data = temp.value()
		if(self.unit=='F'):
			self.data = self.data * 9.0/5.0 + 32.0

		return self.data