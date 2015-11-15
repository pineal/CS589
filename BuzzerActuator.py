from AbstractActuator import AbstractActuator
import pyupm_buzzer as upmBuzzer

class BuzzerActuator(AbstractActuator):

	def __init__(object,pin):
		self.buzzer=upmBuzzer(pin)

	def trigger(self):
		print "Bzzzzzzzz"
		self.buzzer.playSound(upmBuzzer.DO)