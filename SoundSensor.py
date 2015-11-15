import pyupm_mic as upmMicrophone
from AbstractSensor import AbstractSensor

class LightSensor(AbstractSensor):

	def __init__(self,pin):
		self.soundSensor = upmMicrophone.Microphone(pin)

	def readData(self):
		self.data = self.soundSensor.value()

		return self.data