from AbstractActuator import AbstractActuator

class ToggleLcdDisplayMenuActuator(object):
	def __init__(self,lcdDisplay):
		self.lcdDisplay=lcdDisplay

	def trigger(self):
		self.lcdDisplay.toggleDisplayMenu()