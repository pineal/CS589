import pyupm_gas as TP401
from AbstractSensor import AbstractSensor

class AirSensor(AbstractSensor):

	def __init__(self,pin):
		self.airSensor = TP401.TP401(pin)

	def readData(self):
		self.data = self.airSensor.getPPM()

		return self.data