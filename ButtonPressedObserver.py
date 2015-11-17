from AbstractObserver import AbstractObserver

class ButtonPressedObserver(AbstractObserver):

	def __init__(self,buttonSensorProxy,events):
            super(ButtonPressedObserver,self).__init__(events)
            self.buttonSensorProxy=buttonSensorProxy
            self.released=True

	def notify(self):
            if(self.released==True and self.buttonSensorProxy.data==1):
            	self.released=False
                for e in self.events:
                    if(e.thrown==False):
                        e.throw()

            elif(self.buttonSensorProxy.data==0):
            	self.released=True