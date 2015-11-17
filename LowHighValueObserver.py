from AbstractObserver import AbstractObserver

class LowHighValueObserver(AbstractObserver):

	def __init__(self,sensorProxy, lowValue, lowEvents, highValue,highEvents,normalEvents=[]):
            self.sensorProxy=sensorProxy
            self.lowValue=lowValue
            self.highValue=highValue
            self.lowEvents=lowEvents
            self.highEvents=highEvents
            self.normalEvents=normalEvents

	def notify(self):
            if(self.sensorProxy.data>=self.highValue):
                for e in self.highEvents:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True

                for e in self.normalEvents:
                    if(e.thrown==True):
                        e.thrown=False

            elif(self.sensorProxy.data<=self.lowValue):
                for e in self.lowEvents:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True

                for e in self.normalEvents:
                    if(e.thrown==True):
                        e.thrown=False
            else:
                for e in self.normalEvents:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True

                for e in self.highEvents:
                    if(e.thrown==True):
                        e.thrown=False

                for e in self.lowEvents:
                    if(e.thrown==True):
                        e.thrown=False