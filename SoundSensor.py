import pyupm_mic as upmMicrophone
from AbstractSensor import AbstractSensor

class SoundSensor(AbstractSensor):

	def __init__(self,pin):
		self.soundSensor = upmMicrophone.Microphone(pin)

	def readData(self):
		while(1):
			buffer = upmMicrophone.uint16Array(128)
			len = myMic.getSampledWindow(2, 128, buffer);
			if len:
				thresh = myMic.findThreshold(threshContext, 30, buffer, len)
				myMic.printGraph(threshContext)
				if(thresh):
					return thresh