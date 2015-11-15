import pyupm_i2clcd as lcd
from AbstractDisplay import AbstractDisplay
from MyOrderedDict import MyOrderedDict

class LCDDisplay(AbstractDisplay):

	def __init__(self,lcd_address,rgb_address,period):
		super(LCDDisplay,self).__init__(period)
		self.lcdDisplay=lcd.Jhd1313m1(0, lcd_address, rgb_address)
		self.displayMenus=MyOrderedDict()

	def render(self):
		self.lcdDisplay.setColor(255, 0, 0)
		self.currentDisplayMenu.render()
		self.lcdDisplay.setCursor(0,0)
		self.lcdDisplay.write(self.currentDisplayMenu.firstLine)
		self.lcdDisplay.setCursor(1,0)
		self.lcdDisplay.write(self.currentDisplayMenu.secondLine)

	def addDisplayMenu(self,displayMenuName,displayMenu):
		self.displayMenus[displayMenuName]=displayMenu

	def setCurrentDisplayMenu(self,displayMenuName):
		print "Set" + displayMenuName
		self.currentDisplayMenu=self.displayMenus[displayMenuName]
		self.render()

	def toggleDisplayMenu(self):
		print "Toggling"
		setCurrentDisplayMenu(self.displayMenus.nextKey(self.currentDisplayMenu))