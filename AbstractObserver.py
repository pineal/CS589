class AbstractObserver(object):

	def __init__(self,sensorProxies,events):
		self.sensorProxies=sensorProxies
		self.events=events

	def notify(self):
		raise NotImplementedError( "Should have implemented this" )