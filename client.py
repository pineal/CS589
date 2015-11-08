import SensorProxy
import TemperatureSensor
# import BuzzerActuator
import HighTemperatureEvent
import HighTemperatureObserver

# Sensors
temperatureSensor = TemperatureSensor.TemperatureSensor()

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy.SensorProxy(temperatureSensor, 1)

# Actuators
# buzzerActuator=BuzzerActuator()

# Events (Initialize with actuators)
highTemperatureEvent = HighTemperatureEvent.HighTemperatureEvent()

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighTemperatureObserver.HighTemperatureObserver([temperatureSensorProxy],
                                                                          [highTemperatureEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)

temperatureSensorProxy.start()
