import time

from SensorProxy import SensorProxy
from TemperatureSensor import TemperatureSensor
from ButtonSensor import ButtonSensor
from BuzzerActuator import BuzzerActuator
from ToggleLcdDisplayMenuActuator import ToggleLcdDisplayMenuActuator
from HighTemperatureObserver import HighTemperatureObserver
from ButtonPressedObserver import ButtonPressedObserver
from Event import Event

from LCDDisplayMenu import LCDDisplayMenu
from LCDDisplay import LCDDisplay

#Display
lcdDisplay=LCDDisplay(0x3E, 0x62,1)

# Sensors
temperatureSensor = TemperatureSensor(0,'C')
buttonSensor = ButtonSensor(3)

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor, 2)
buttonSensorProxy = SensorProxy(buttonSensor, 1)

# Actuators
buzzerActuator=BuzzerActuator()
toggleLcdDisplayMenuActuator=ToggleLcdDisplayMenuActuator(lcdDisplay)

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator])
buttonPressedEvent=Event([buzzerActuator,toggleDisplayMenuActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighTemperatureObserver(temperatureSensorProxy,24,[highTemperatureEvent])
buttonPressedObserver = ButtonPressedObserver(buttonSensorProxy,[buttonPressedEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)
buttonSensorProxy.addObserver(buttonPressedObserver)

#Display Menus
temperatureDisplayMenu=LCDDisplayMenu(["Temperature:",temperatureSensorProxy," C"],["Button Status: ",buttonSensorProxy])
buttonDisplayMenu=LCDDisplayMenu(["Button Status",buttonSensorProxy],[])

lcdDisplay.addDisplayMenu('temperature',temperatureDisplayMenu)
lcdDisplay.addDisplayMenu('button',temperatureDisplayMenu)

lcdDisplay.setCurrentDisplayMenu('temperature')

temperatureSensorProxy.start()
buttonSensorProxy.start()
lcdDisplay.start()
while 1:
    time.sleep(5)