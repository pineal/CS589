import threading
import time
from collections import deque

class SensorProxy(threading.Thread):
	def __init__(self,sensor,period,precision=1,smoothing=1,dismiss=0):
		threading.Thread.__init__(self)
		self.sensor=sensor
		self.observers=[]
		self.period=period
		self.data=0

		self.precision=precision

		self.smoothing=smoothing
		self.readings=deque(self.smoothing*[0],self.smoothing)
		self.readingsCounter=0

		self.dismiss=dismiss
		self.dismissCounter=0

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

		if(self.dismissCounter<self.dismiss):
			self.sensor.readData()#Dismiss reading
			self.dismissCounter=self.dismissCounter+1
			self.data="Initializing"
			return

		#Smooth readings and round result
		self.readings.append(self.sensor.readData())

		if(self.readingsCounter<self.smoothing):
			self.readingsCounter=self.readingsCounter+1

		self.data=round(sum(self.readings)/float(self.readingsCounter),self.precision)

		self.notifyObservers()

	def addObserver(self,observer):
		self.observers.append(observer)