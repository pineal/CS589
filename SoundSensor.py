import pyupm_mic as upmMicrophone
from AbstractSensor import AbstractSensor

class SoundSensor(AbstractSensor):

	def __init__(self,pin):
		self.soundSensor = upmMicrophone.Microphone(pin)

	def readData(self):
		while(1):
			buffer = upmMicrophone.uint16Array(128)
			len = self.soundSensor.getSampledWindow(2, 128, buffer);
			if len:
				thresh = self.soundSensor.findThreshold(threshContext, 30, buffer, len)
				self.soundSensor.printGraph(threshContext)
				if(thresh):
					return thresh