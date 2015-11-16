import time

from SensorProxy import SensorProxy
from TemperatureSensor import TemperatureSensor
from LightSensor import LightSensor
from AirSensor import AirSensor
from SoundSensor import SoundSensor
from ButtonSensor import ButtonSensor
from BuzzerActuator import BuzzerActuator
from ToggleLcdDisplayMenuActuator import ToggleLcdDisplayMenuActuator
from HighValueObserver import HighValueObserver
from ButtonPressedObserver import ButtonPressedObserver
from Event import Event

from LCDDisplayMenu import LCDDisplayMenu
from LCDDisplay import LCDDisplay

#Display
lcdDisplay=LCDDisplay(0x3E, 0x62,1)

# Sensors
temperatureSensor = TemperatureSensor(0,'C')
buttonSensor = ButtonSensor(3)
lightSensor = LightSensor(1)
soundSensor = SoundSensor(2)
airSensor=AirSensor(3)

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor, 2,1,10)
buttonSensorProxy = SensorProxy(buttonSensor, 0.2)
lightSensorProxy = SensorProxy(lightSensor,0.2)
soundSensorProxy = SensorProxy(soundSensor,0.1)
airSensorProxy = SensorProxy(airSensor,1,2,20)

# Actuators
buzzerActuator=BuzzerActuator(5)
toggleLcdDisplayMenuActuator=ToggleLcdDisplayMenuActuator(lcdDisplay)

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator])
buttonPressedEvent=Event([toggleLcdDisplayMenuActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighValueObserver(temperatureSensorProxy,24,[highTemperatureEvent])
buttonPressedObserver = ButtonPressedObserver(buttonSensorProxy,[buttonPressedEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)
buttonSensorProxy.addObserver(buttonPressedObserver)

#Display Menus
temperatureDisplayMenu=LCDDisplayMenu(["Temp:",temperatureSensorProxy," C"],[])
lightDisplayMenu=LCDDisplayMenu(["Light:",lightSensorProxy," lux"],[])
soundDisplayMenu=LCDDisplayMenu(["Sound Level:",soundSensorProxy],[])
buttonDisplayMenu=LCDDisplayMenu(["Button Status: ",buttonSensorProxy],[])
airDisplayMenu=LCDDisplayMenu(["Air: ",airSensorProxy, " ppm"],[])

lcdDisplay.addDisplayMenu('temperature',temperatureDisplayMenu)
lcdDisplay.addDisplayMenu('button',buttonDisplayMenu)
lcdDisplay.addDisplayMenu('light',lightDisplayMenu)
lcdDisplay.addDisplayMenu('sound',soundDisplayMenu)
lcdDisplay.addDisplayMenu('air',airDisplayMenu)

lcdDisplay.setCurrentDisplayMenu('temperature')

temperatureSensorProxy.start()
lightSensorProxy.start()
soundSensorProxy.start()
airSensorProxy.start()
buttonSensorProxy.start()
lcdDisplay.start()
while 1:
    time.sleep(5)