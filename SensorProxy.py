import threading
import time

class SensorProxy(threading.Thread):
	def __init__(self,sensor,period):
		threading.Thread.__init__(self)
		self.sensor=sensor
		self.observers=[]
		self.period=period
		self.data=0

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
		self.data=self.sensor.readData()
		print "Updated Sensor Data:" + str(self.data)
		self.notifyObservers()

	def addObserver(self,observer):
		self.observers.append(observer)