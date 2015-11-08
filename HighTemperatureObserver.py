from AbstractObserver import AbstractObserver

class HighTemperatureObserver(AbstractObserver):

	def __init__(self,sensorProxies,events):
		super(HighTemperatureObserver,self).__init__(sensorProxies,events)

	def notify(self):
			print "HighTemperatureObserver Notified"