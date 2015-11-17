from AbstractObserver import AbstractObserver

class HighValueObserver(AbstractObserver):

	def __init__(self,sensorProxy, highValue,highEvents,normalEvents=[]):
            super(HighValueObserver,self).__init__(highEvents)
            self.sensorProxy=sensorProxy
            self.highValue=highValue
            self.normalEvents=normalEvents

	def notify(self):
            if(self.sensorProxy.data>self.highValue):
                for e in self.events:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True

                for e in self.normalEvents:
                    if(e.thrown==True):
                        e.thrown=False
            #TODO Change this to be more graceful
            else:
                for e in self.normalEvents:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True

                for e in self.events:
                    if(e.thrown==True):
                        e.thrown=False