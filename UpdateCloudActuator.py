from AbstractActuator import AbstractActuator
import json
from json import encoder

class UpdateCloudActuator(AbstractActuator):

	def __init__(self,cloudUrl,sensorProxies):
		self.cloudUrl=cloudUrl
		self.sensorProxies=sensorProxies
		self.payload={}
		encoder.FLOAT_REPR = lambda o: format(o, '.2f')

	def trigger(self):
		print "Update request sent to the cloud"
		self.updateCloud()

	def updateCloud(self):
		for sensorProxy in self.sensorProxies:
			self.payload[sensorProxy.name]=sensorProxy.data

		print json.dumps(self.payload)
