from AbstractActuator import AbstractActuator
import json
import requests

class UpdateCloudActuator(AbstractActuator):

	def __init__(self,cloudUrl,sensorProxies):
		self.cloudUrl=cloudUrl
		self.sensorProxies=sensorProxies
		self.payload={}

	def trigger(self):
		print "Update request sent to the cloud"
		self.updateCloud()

	def updateCloud(self):
		for sensorProxy in self.sensorProxies:
			self.payload[sensorProxy.name]=str(sensorProxy.data)

		r=requests.post(self.cloudUrl,json=self.payload)
		print 'Sent the following update to the cloud:'
		print self.payload
