import threading
import time

class AbstractDisplay(threading.Thread):

	def __init__(self,period):
		threading.Thread.__init__(self)
		self.period=period

	def render(self):
		raise NotImplementedError("Should have implemented this")

	def run(self):
		print "Starting SensorProxy thread"
		var = 1
		while var==1:
			time.sleep(self.period)
			self.render()