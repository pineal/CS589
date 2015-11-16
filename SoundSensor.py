import pyupm_mic as upmMicrophone
from AbstractSensor import AbstractSensor

class SoundSensor(AbstractSensor):

	def __init__(self,pin):
		self.soundSensor = upmMicrophone.Microphone(pin)
		self.threshContext = upmMicrophone.thresholdContext()
		self.threshContext.averageReading=0
		self.threshContext.runningAverage=0
		self.threshContext.averagedOver=2

	def readData(self):
		while(1):
			buffer = upmMicrophone.uint16Array(128)
			len = self.soundSensor.getSampledWindow(2, 128, buffer);
			if len:
				thresh = self.soundSensor.findThreshold(self.threshContext, 30, buffer, len)
				if(thresh):
					self.data=thresh
					return self.data