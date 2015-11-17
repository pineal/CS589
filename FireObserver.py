from AbstractObserver import AbstractObserver

class FireObserver(AbstractObserver):

	def __init__(self,temperatureSensorProxy,fireTemperature,airSensorProxy,fireAir,events):
            super(FireObserver,self).__init__(events)
            self.temperatureSensorProxy=temperatureSensorProxy
            self.airSensorProxy=airSensorProxy
            self.fireTemperature=fireTemperature
            self.fireAir=fireAir

	def notify(self):
            print "Notified"
            print "Temperatue: " + self.temperatureSensorProxy.data
            print "Air: " + self.airSensorProxy.data
            if(self.temperatureSensorProxy.data>=self.fireTemperature and self.airSensorProxy.data>=self.fireAir):
                for e in self.events:
                        e.throw()