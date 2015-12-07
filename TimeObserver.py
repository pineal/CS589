from AbstractObserver import AbstractObserver

class TimeObserver(AbstractObserver):

	def __init__(self,events):
		super(TimeObserver,self).__init__(events)

	def notify(self):
		for e in self.events:
			e.throw()