import threading
import time
from collections import deque

class SensorProxy(threading.Thread):
	def __init__(self,sensor,period,smoothing=1):
		threading.Thread.__init__(self)
		self.sensor=sensor
		self.observers=[]
		self.period=period
		self.data=0

		self.smoothing=smoothing
		self.readings=deque(self.smoothing*[0],self.smoothing)

	def run(self):
		print "Starting SensorProxy thread"
		var = 1
		while var==1:
			time.sleep(self.period)
			self.update()

	def notifyObservers(self):
		for observer in self.observers:
			observer.notify()

	def update(self):
		
		self.readings.append(self.sensor.readData())
		self.data=sum(self.readings)/float(self.smoothing)
		self.notifyObservers()

	def addObserver(self,observer):
		self.observers.append(observer)