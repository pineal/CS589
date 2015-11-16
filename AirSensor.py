import pyupm_gas as TP401
from AbstractSensor import AbstractSensor

class AirSensor(AbstractSensor):

	def __init__(self,pin):
		self.airSensor = TP401.TP401(pin)

	def readData(self):
		self.sample=self.airSensor.getSample()
		self.data = self.airSensor.getPPM()
		print "PPM: " + str(self.data)
		print "Raw: " + str(self.sample)
		return self.data