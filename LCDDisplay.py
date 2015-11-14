import pyupm_i2clcd as lcd
from AbstractDisplay import AbstractDisplay

class LCDDisplay(AbstractDisplay):

	def __init__(self,lcd_address,rgb_address):
		self.lcdDisplay=lcd.Jhd1313m1(0, lcd_address, rgb_address)
		self.lcdDisplay.setCursor(0,0)
		self.lcdDisplay.setColor(255, 0, 0)
		self.data="Hello World"

	def render(self):
		self.lcdDisplay.write(self.data)