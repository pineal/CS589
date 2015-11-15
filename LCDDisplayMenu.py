from SensorProxy import SensorProxy

class LCDDisplayMenu(object):
	def __init__(self,firstLineEntities,secondLineEntities):
		self.firstLineEntities=firstLineEntities
		self.secondLineEntities=secondLineEntities
		self.firstLine=""
		self.secondLine=""

	def render(self):
		for entity in firstLineEntities:
			if(isinstance(entity,SensorProxy)):
				self.firstLine+=str(entity.data)
			else if(isinstance(entity,str)):
				self.firstLine+=entity

		for entity in secondLineEntities:
			if(isinstance(entity,SensorProxy)):
				self.secondLine+=str(entity.data)
			else if(isinstance(entity,str)):
				self.secondLine+=entity