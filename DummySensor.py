from AbstractSensor import AbstractSensor

class DummySensor(AbstractSensor):

	def readData(self):
		return 0