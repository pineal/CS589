from AbstractSensor import AbstractSensor
import pyump_grove as grove

class ButtonSensor(AbstractSensor):

	def __init__(self,pin):
		self.button=grove.GroveButton(pin)

	def readData(self):
            return self.button.value()