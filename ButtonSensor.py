import pyump_grove as grove
from AbstractSensor import AbstractSensor

class ButtonSensor(AbstractSensor):

	def __init__(self,pin):
		self.button=grove.GroveButton(pin)

	def readData(self):
            return self.button.value()