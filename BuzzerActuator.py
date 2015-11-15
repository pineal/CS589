from AbstractActuator import AbstractActuator
import pyupm_buzzer as upmBuzzer

class BuzzerActuator(AbstractActuator):

	def __init__(self,pin):
		self.buzzer=upmBuzzer.Buzzer(pin)

	def trigger(self):
		print "Bzzzzzzzz"
		self.buzzer.playSound(upmBuzzer.DO)