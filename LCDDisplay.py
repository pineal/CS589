import pyupm_i2clcd as lcd
from AbstractDisplay import AbstractDisplay

class LCDDisplay(AbstractDisplay):

	def __init__(self,lcd_address,rgb_address,period):
		super(LCDDisplay,self).__init__(period)
		self.lcdDisplay=lcd.Jhd1313m1(0, lcd_address, rgb_address)
		self.displayMenus={}

	def render(self):
		print "Rendering..."
		self.lcdDisplay.setColor(255, 0, 0)
		self.currentDisplayMenu.render()
		self.lcdDisplay.setCursor(0,0)
		self.lcdDisplay.write(self.currentDisplayMenu.firstLine)
		self.lcdDisplat.setCursor(1,0)
		self.lcdDisplay.write(self.currentDisplayMenu.secondLine)

	def addDisplayMenu(self,displayMenuName,displayMenu):
		self.displayMenus[displayMenuName]=displayMenu

	def setCurrentDisplayMenu(displayMenuName):
		self.currentDisplayMenu=displayMenus[displayMenuName]
		self.render()