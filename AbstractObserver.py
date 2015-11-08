class AbstractObserver(object):

	def __init__(self,events):
		self.events=events

	def notify(self):
		raise NotImplementedError( "Should have implemented this" )