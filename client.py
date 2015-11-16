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
from ChangeLCDDisplayMenuBackgroundColorActuator import ChangeLCDDisplayMenuBackgroundColorActuator
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

# Actuators
buzzerActuator=BuzzerActuator(5)
toggleLcdDisplayMenuActuator=ToggleLcdDisplayMenuActuator(lcdDisplay)

temperatureHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,255,0,0)
temperatureNoBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,0,0,0)
lightHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(lightDisplayMenu,255,0,0)
soundHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(soundDisplayMenu,255,0,0)
airHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(airDisplayMenu,255,0,0)

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator,temperatureHighValueRedBackgroundActuator])
lowTemperatureEvent = Event([temperatureLowValueNoBackgroundActuator])
buttonPressedEvent=Event([toggleLcdDisplayMenuActuator,temperatureLowValueRedBackgroundActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighValueObserver(temperatureSensorProxy,20,[highTemperatureEvent])
lowTemperatureObserver = LowValueObserver(temperatureSensorProxy,10,[lowTemperatureEvent])
buttonPressedObserver = ButtonPressedObserver(buttonSensorProxy,[buttonPressedEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)
buttonSensorProxy.addObserver(buttonPressedObserver)

temperatureSensorProxy.start()
lightSensorProxy.start()
soundSensorProxy.start()
airSensorProxy.start()
buttonSensorProxy.start()
lcdDisplay.start()
while 1:
    time.sleep(5)