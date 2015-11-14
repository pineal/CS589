import time

from SensorProxy import SensorProxy
from TemperatureSensor import TemperatureSensor
from ButtonSensor import ButtonSensor
from BuzzerActuator import BuzzerActuator
from HighTemperatureObserver import HighTemperatureObserver
from ButtonPressedObserver import ButtonPressedObserver
from Event import Event


# Sensors
temperatureSensor = TemperatureSensor()
buttonSensor = ButtonSensor(3)

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor, 2)
buttonSensorProxy = SensorProxy(buttonSensor, 1)

# Actuators
buzzerActuator=BuzzerActuator()

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator])
buttonPressedEvent=Event([buzzerActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighTemperatureObserver(temperatureSensorProxy,5,[highTemperatureEvent])
buttonPressedObserver = ButtonPressedObserver(buttonSensorProxy,[buttonPressedEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)
buttonSensorProxy.addObserver(buttonPressedObserver)

#temperatureSensorProxy.start()
buttonSensorProxy.start()

while 1:
    time.sleep(5)