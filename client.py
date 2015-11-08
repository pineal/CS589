from SensorProxy import SensorProxy
from TemperatureSensor import TemperatureSensor
from BuzzerActuator import BuzzerActuator
from HighTemperatureObserver import HighTemperatureObserver
from Event import Event

# Sensors
temperatureSensor = TemperatureSensor()

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor, 1)

# Actuators
buzzerActuator=BuzzerActuator()

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighTemperatureObserver(temperatureSensorProxy,10,[highTemperatureEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)

temperatureSensorProxy.start()
