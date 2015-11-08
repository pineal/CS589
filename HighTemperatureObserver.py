from AbstractObserver import AbstractObserver

class HighTemperatureObserver(AbstractObserver):

	def __init__(self,temperatureSensorProxy, highValue,events):
            super(HighTemperatureObserver,self).__init__(events)
            self.temperatureSensorProxy=temperatureSensorProxy
            self.highValue=highValue

	def notify(self):
            print "HighTemperatureObserver Notified"
            if(self.temperatureSensorProxy.data>self.highValue):
                for e in self.events:
                    if(e.thrown==False):
                        e.throw()
                        e.thrown=True
            #TODO Change this to be more graceful
            else:
                for e in self.events:
                    if(e.thrown==True):
                        e.thrown=False