from AbstractObserver import AbstractObserver

class ButtonPressedObserver(AbstractObserver):

	def __init__(self,buttonSensorProxy,events):
            super(ButtonPressedObserver,self).__init__(events)
            self.buttonSensorProxy=buttonSensorProxy

	def notify(self):
            print "ButtonPressedObserver Notified"
            if(self.buttonSensorProxy.data==1):
                for e in self.events:
                    if(e.thrown==False):
                        e.throw()