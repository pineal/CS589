from AbstractSensor import AbstractSensor

class TemperatureSensor(AbstractSensor):

	def __init__(self):
		self.data=1
		pass

	def readData(self):
		self.data=self.data+1
		return self.data