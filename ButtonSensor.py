from AbstractSensor import AbstractSensor

class ButtonSensor(AbstractSensor):

	def __init__(self):
		pass

	def readData(self):
            tmp=raw_input()
            if(tmp=='a'):
                return 1
            else:
                return 0