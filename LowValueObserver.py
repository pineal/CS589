from AbstractObserver import AbstractObserver

class LowValueObserver(AbstractObserver):

    def __init__(self,sensorProxy, lowValue,lowEvents,normalEvents=[]):
            super(LowValueObserver,self).__init__(lowEvents)
            self.sensorProxy=sensorProxy
            self.lowValue=lowValue
            self.normalEvents=normalEvents

    def notify(self):
            if(self.sensorProxy.data<self.lowValue):
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