from AbstractActuator import AbstractActuator

class ChangeLCDDisplayMenuBackgroundColorActuator(object):

	def __init__(self,lcdDisplayMenu,R,G,B):
		self.lcdDisplayMenu=lcdDisplayMenu
		self.R=R
		self.G=G
		self.B=B

	def trigger(self):
		self.lcdDisplayMenu.R=self.R
		self.lcdDisplayMenu.G=self.G
		self.lcdDisplayMenu.B=self.B