from AbstractActuator import AbstractActuator

class ChangeLCDDisplayMenuBackgroundColorActuator(object):

	def __init__(self,lcdDisplayMenu,R,G,B):
		self.lcdDisplayMenu=lcdDisplayMenu
		self.R=R
		self.G=G
		self.B=B

	def trigger(self):
		lcdDisplayMenu.R=self.R
		lcdDisplayMenu.G=self.G
		lcdDisplayMenu.B=self.B