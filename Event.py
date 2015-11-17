class Event(object):

	def __init__(self,actuators):
		self.actuators=actuators
		self.thrown=False

	def throw(self):
		for a in self.actuators:
			a.trigger()