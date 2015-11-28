from AbstractActuator import AbstractActuator

class UpdateCloudActuator(AbstractActuator):

	def __init__(self,cloudUrl,sensorProxies):
		self.cloudUrl=cloudUrl
		self.sensorProxies=sensorProxies

	def trigger(self):
		print "Update request sent to the cloud"
		updateCloud()

	def updateCloud(self):
		pass
