from SensorProxy import SensorProxy
from TemperatureSensor import TemperatureSensor
# import BuzzerActuator
from HighTemperatureEvent import HighTemperatureEvent
from HighTemperatureObserver import HighTemperatureObserver

# Sensors
temperatureSensor = TemperatureSensor()

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor, 1)

# Actuators
# buzzerActuator=BuzzerActuator()

# Events (Initialize with actuators)
highTemperatureEvent = HighTemperatureEvent()

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighTemperatureObserver([temperatureSensorProxy],
                                                                          [highTemperatureEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)

temperatureSensorProxy.start()
