from AbstractObserver import AbstractObserver

class HighValueObserver(AbstractObserver):

	def __init__(self,sensorProxy, highValue,events):
            super(HighValueObserver,self).__init__(events)
            self.sensorProxy=sensorProxy
            self.highValue=highValue

	def notify(self):
            if(self.sensorProxy.data>self.highValue):
                for e in self.events:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True
            #TODO Change this to be more graceful
            else:
                for e in self.events:
                    if(e.thrown==True):
                        e.thrown=False