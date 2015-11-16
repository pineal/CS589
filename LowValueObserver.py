from AbstractObserver import AbstractObserver

class LowValueObserver(AbstractObserver):

	def __init__(self,sensorProxy, lowValue,events):
            super(LowValueObserver,self).__init__(events)
            self.sensorProxy=sensorProxy
            self.lowValue=lowValue

	def notify(self):
            if(self.sensorProxy.data<self.lowValue):
                for e in self.events:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True
            #TODO Change this to be more graceful
            else:
                for e in self.events:
                    if(e.thrown==True):
                        e.thrown=False