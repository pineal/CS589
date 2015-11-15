import pyupm_grove as grove
from AbstractSensor import AbstractSensor

class LightSensor(AbstractSensor):

	def __init__(self,pin,unit):
		self.lightSensor = grove.GroveLight(pin)
		self.unit = unit
		pass

	def readData(self):
		self.data = self.lightSensor.value()

		return self.data