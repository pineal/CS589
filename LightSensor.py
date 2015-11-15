import pyupm_grove as grove
from AbstractSensor import AbstractSensor

class LightSensor(AbstractSensor):

	def __init__(self,pin):
		self.lightSensor = grove.GroveLight(pin)

	def readData(self):
		self.data = self.lightSensor.value()

		return self.data