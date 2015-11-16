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
from LowValueObserver import LowValueObserver
from ButtonPressedObserver import ButtonPressedObserver
from ChangeLCDDisplayMenuBackgroundColorActuator import ChangeLCDDisplayMenuBackgroundColorActuator
from Event import Event

from LCDDisplayMenu import LCDDisplayMenu
from LCDDisplay import LCDDisplay

##############################################
#I/O Constants
##############################################

#LCD
LCDDISPLAY_ADDRESS=0x3E
LCDDISPLAY_RGBADDRESS=0x62
LCDDISPLAY_REFRESH_PERIOD=1

#Temperature Sensor
TEMPERATURE_SENSOR_A_PIN=0
TEMPERATURE_SENSOR_UNIT='C'
TEMPERATURE_SENSOR_REFRESH_PERIOD=2
TEMPERATURE_SENSOR_PRECISION=1
TEMPERATURE_SENSOR_AVERAGE_SAMPLES=10

#Button Sensor
BUTTON_SENSOR_D_PIN=3
BUTTON_SENSOR_REFRESH_PERIOD=0.2

#Light Sensor
LIGHT_SENSOR_A_PIN=1
LIGHT_SENSOR_REFRESH_PERIOD=0.2
LIGHT_SENSOR_UNIT='lux'

#Sound Sensor
SOUND_SENSOR_A_PIN=2
SOUND_SENSOR_REFRESH_PERIOD=0.1

#Air Sensor
AIR_SENSOR_A_PIN=3
AIR_SENSOR_REFRESH_PERIOD=1
AIR_SENSOR_PRECISION=2
AIR_SENSOR_AVERAGE_SAMPLES=20
AIR_SENSOR_UNIT='ppm'

#Buzzer Actuator
BUZZER_ACTUATOR_D_PIN=5
##############################################
#Observer Constants
##############################################
HIGH_TEMPERATURE=20
LOW_TEMPERATURE=10

HIGH_SOUND=0
LOW_SOUND=0

HIGH_LIGHT=0
LOW_LIGHT=0

HIGH_AIR=0
LOW_AIR=0
##############################################

##############################################
#Sub-systems Configuation
##############################################

#Display
lcdDisplay=LCDDisplay(LCDDISPLAY_ADDRESS, LCDDISPLAY_RGBADDRESS,LCDDISPLAY_REFRESH_PERIOD)

# Sensors
temperatureSensor = TemperatureSensor(TEMPERATURE_SENSOR_A_PIN,TEMPERATURE_SENSOR_UNIT)
buttonSensor = ButtonSensor(BUTTON_SENSOR_D_PIN)
lightSensor = LightSensor(LIGHT_SENSOR_A_PIN)
soundSensor = SoundSensor(SOUND_SENSOR_A_PIN)
airSensor=AirSensor(AIR_SENSOR_A_PIN)

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor,TEMPERATURE_SENSOR_REFRESH_PERIOD,TEMPERATURE_SENSOR_PRECISION,TEMPERATURE_SENSOR_AVERAGE_SAMPLES)
buttonSensorProxy = SensorProxy(buttonSensor, BUTTON_SENSOR_REFRESH_PERIOD)
lightSensorProxy = SensorProxy(lightSensor,LIGHT_SENSOR_REFRESH_PERIOD)
soundSensorProxy = SensorProxy(soundSensor,SOUND_SENSOR_REFRESH_PERIOD)
airSensorProxy = SensorProxy(airSensor,AIR_SENSOR_REFRESH_PERIOD,AIR_SENSOR_PRECISION,AIR_SENSOR_AVERAGE_SAMPLES)

#Display Menus
temperatureDisplayMenu=LCDDisplayMenu(["Temp:",temperatureSensorProxy," ",TEMPERATURE_SENSOR_UNIT],[])
lightDisplayMenu=LCDDisplayMenu(["Light:",lightSensorProxy," ",LIGHT_SENSOR_UNIT],[])
soundDisplayMenu=LCDDisplayMenu(["Sound Level:",soundSensorProxy],[])
buttonDisplayMenu=LCDDisplayMenu(["Button Status: ",buttonSensorProxy],[])
airDisplayMenu=LCDDisplayMenu(["Air: ",airSensorProxy, " ",AIR_SENSOR_UNIT],[])

lcdDisplay.addDisplayMenu('temperature',temperatureDisplayMenu)
lcdDisplay.addDisplayMenu('button',buttonDisplayMenu)
lcdDisplay.addDisplayMenu('light',lightDisplayMenu)
lcdDisplay.addDisplayMenu('sound',soundDisplayMenu)
lcdDisplay.addDisplayMenu('air',airDisplayMenu)

lcdDisplay.setCurrentDisplayMenu('temperature')

# Actuators
buzzerActuator=BuzzerActuator(BUZZER_ACTUATOR_D_PIN)
toggleLcdDisplayMenuActuator=ToggleLcdDisplayMenuActuator(lcdDisplay)

temperatureHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,255,0,0)
temperatureLowValueNoBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,255,255,255)
lightHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(lightDisplayMenu,255,0,0)
soundHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(soundDisplayMenu,255,0,0)
airHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(airDisplayMenu,255,0,0)

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator,temperatureHighValueRedBackgroundActuator])
lowTemperatureEvent = Event([temperatureLowValueNoBackgroundActuator])
buttonPressedEvent=Event([toggleLcdDisplayMenuActuator,temperatureLowValueNoBackgroundActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
highTemperatureObserver = HighValueObserver(temperatureSensorProxy,HIGH_TEMPERATURE,[highTemperatureEvent])
lowTemperatureObserver = LowValueObserver(temperatureSensorProxy,LOW_TEMPERATURE,[lowTemperatureEvent])
buttonPressedObserver = ButtonPressedObserver(buttonSensorProxy,[buttonPressedEvent])

# Add Observers
temperatureSensorProxy.addObserver(highTemperatureObserver)
buttonSensorProxy.addObserver(buttonPressedObserver)

##############################################
#Start Sub-systems
##############################################
temperatureSensorProxy.start()
lightSensorProxy.start()
soundSensorProxy.start()
airSensorProxy.start()
buttonSensorProxy.start()
lcdDisplay.start()