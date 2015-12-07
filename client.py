import time

from SensorProxy import SensorProxy
from TemperatureSensor import TemperatureSensor
from LightSensor import LightSensor
from AirSensor import AirSensor
from SoundSensor import SoundSensor
from ButtonSensor import ButtonSensor
from DummySensor import DummySensor
from BuzzerActuator import BuzzerActuator
from UpdateCloudActuator import UpdateCloudActuator
from ToggleLcdDisplayMenuActuator import ToggleLcdDisplayMenuActuator
from HighValueObserver import HighValueObserver
from LowValueObserver import LowValueObserver
from LowHighValueObserver import LowHighValueObserver
from ButtonPressedObserver import ButtonPressedObserver
from TimeObserver import TimeObserver
from FireObserver import FireObserver
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
LCDDISPLAY_REFRESH_PERIOD=0.3

#Temperature Sensor
TEMPERATURE_SENSOR_A_PIN=0
TEMPERATURE_SENSOR_UNIT='C'
TEMPERATURE_SENSOR_REFRESH_PERIOD=2
TEMPERATURE_SENSOR_PRECISION=1
TEMPERATURE_SENSOR_AVERAGE_SAMPLES=20
TEMPERATURE_SENSOR_MACHINE_NAME='temperature'

#Button Sensor
BUTTON_SENSOR_D_PIN=3
BUTTON_SENSOR_REFRESH_PERIOD=0.1
BUTTON_SENSOR_MACHINE_NAME='button0'

#Light Sensor
LIGHT_SENSOR_A_PIN=1
LIGHT_SENSOR_REFRESH_PERIOD=0.2
LIGHT_SENSOR_UNIT='lux'
LIGHT_SENSOR_MACHINE_NAME='light'

#Sound Sensor
SOUND_SENSOR_A_PIN=2
SOUND_SENSOR_REFRESH_PERIOD=1
SOUND_SENSOR_PRECISION=1
SOUND_SENSOR_AVERAGE_SAMPLES=4
SOUND_SENSOR_MACHINE_NAME='sound'

#Air Sensor
AIR_SENSOR_A_PIN=3
AIR_SENSOR_REFRESH_PERIOD=1
AIR_SENSOR_PRECISION=2
AIR_SENSOR_AVERAGE_SAMPLES=20
AIR_SENSOR_UNIT='ppm'
AIR_SENSOR_MACHINE_NAME='air'

###############################
#Cloud updates
CLOUD_SENSOR_REFRESH_PERIOD=10
CLOUD_UPDATE_URL='http://localhost:8080/send'
###############################

#Buzzer Actuator
BUZZER_ACTUATOR_D_PIN=5
##############################################
#Observer Constants
##############################################
HIGH_TEMPERATURE=22
LOW_TEMPERATURE=10

HIGH_SOUND=600

HIGH_LIGHT=70

HIGH_AIR=30

FIRE_TEMPERATURE=30
FIRE_AIR=70
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
dummySensor=DummySensor()

# SensorProxies (Initialize with sensor)
temperatureSensorProxy = SensorProxy(temperatureSensor,TEMPERATURE_SENSOR_MACHINE_NAME,TEMPERATURE_SENSOR_REFRESH_PERIOD,TEMPERATURE_SENSOR_PRECISION,TEMPERATURE_SENSOR_AVERAGE_SAMPLES)
buttonSensorProxy = SensorProxy(buttonSensor, BUTTON_SENSOR_MACHINE_NAME,BUTTON_SENSOR_REFRESH_PERIOD)
lightSensorProxy = SensorProxy(lightSensor,LIGHT_SENSOR_MACHINE_NAME,LIGHT_SENSOR_REFRESH_PERIOD)
soundSensorProxy = SensorProxy(soundSensor,SOUND_SENSOR_MACHINE_NAME,SOUND_SENSOR_REFRESH_PERIOD,SOUND_SENSOR_PRECISION,SOUND_SENSOR_AVERAGE_SAMPLES,3)
airSensorProxy = SensorProxy(airSensor,AIR_SENSOR_MACHINE_NAME,AIR_SENSOR_REFRESH_PERIOD,AIR_SENSOR_PRECISION,AIR_SENSOR_AVERAGE_SAMPLES)
timeSensorProxy = SensorProxy(dummySensor,'timer0',CLOUD_SENSOR_REFRESH_PERIOD)

#Display Menus
temperatureDisplayMenu=LCDDisplayMenu(["Temp:",temperatureSensorProxy," ",TEMPERATURE_SENSOR_UNIT],[])
lightDisplayMenu=LCDDisplayMenu(["Light:",lightSensorProxy," ",LIGHT_SENSOR_UNIT],[])
soundDisplayMenu=LCDDisplayMenu(["Sound:",soundSensorProxy],[])
airDisplayMenu=LCDDisplayMenu(["Air: ",airSensorProxy, " ",AIR_SENSOR_UNIT],[])

lcdDisplay.addDisplayMenu('temperature',temperatureDisplayMenu)
lcdDisplay.addDisplayMenu('light',lightDisplayMenu)
lcdDisplay.addDisplayMenu('sound',soundDisplayMenu)
lcdDisplay.addDisplayMenu('air',airDisplayMenu)

lcdDisplay.setCurrentDisplayMenu('temperature')

# Actuators
buzzerActuator=BuzzerActuator(BUZZER_ACTUATOR_D_PIN)
toggleLcdDisplayMenuActuator=ToggleLcdDisplayMenuActuator(lcdDisplay)

temperatureHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,255,0,0)
temperatureNormalValueNoBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,255,255,255)
temperatureLowValueBlueBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(temperatureDisplayMenu,0,0,255)

lightHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(lightDisplayMenu,255,0,0)
lightNormalValueNoBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(lightDisplayMenu,255,255,255)

soundHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(soundDisplayMenu,255,0,0)
soundNormalValueNoBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(soundDisplayMenu,255,255,255)

airHighValueRedBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(airDisplayMenu,255,0,0)
airNormalValueNoBackgroundActuator=ChangeLCDDisplayMenuBackgroundColorActuator(airDisplayMenu,255,255,255)

updateCloudActuator=UpdateCloudActuator(CLOUD_UPDATE_URL,[temperatureSensorProxy,airSensorProxy,soundSensorProxy,lightSensorProxy])

# Events (Initialize with actuators)
highTemperatureEvent = Event([buzzerActuator,temperatureHighValueRedBackgroundActuator])
lowTemperatureEvent = Event([buzzerActuator,temperatureLowValueBlueBackgroundActuator])
normalTemperatureEvent = Event([temperatureNormalValueNoBackgroundActuator])

highLightEvent = Event([buzzerActuator,lightHighValueRedBackgroundActuator])
normalLightEvent = Event([lightNormalValueNoBackgroundActuator])

highSoundEvent = Event([buzzerActuator,soundHighValueRedBackgroundActuator])
normalSoundEvent = Event([soundNormalValueNoBackgroundActuator])

highAirEvent = Event([buzzerActuator,airHighValueRedBackgroundActuator])
normalAirEvent = Event([airNormalValueNoBackgroundActuator])

buttonPressedEvent=Event([toggleLcdDisplayMenuActuator])
fireEvent=Event([buzzerActuator,temperatureHighValueRedBackgroundActuator,airHighValueRedBackgroundActuator])

updateCloudEvent=Event([updateCloudActuator])

# Observers (Initialize with proxies they subscribe to and events that should be raised)
lowHighTemperatureObserver=LowHighValueObserver(temperatureSensorProxy,LOW_TEMPERATURE,[lowTemperatureEvent],HIGH_TEMPERATURE,[highTemperatureEvent],[normalTemperatureEvent])

highLightObserver = HighValueObserver(lightSensorProxy,HIGH_LIGHT,[highLightEvent],[normalLightEvent])

highSoundObserver = LowValueObserver(soundSensorProxy,HIGH_SOUND,[highSoundEvent],[normalSoundEvent])

highAirObserver = HighValueObserver(airSensorProxy,HIGH_AIR,[highAirEvent],[normalAirEvent])

buttonPressedObserver = ButtonPressedObserver(buttonSensorProxy,[buttonPressedEvent])
fireObserver = FireObserver(temperatureSensorProxy,FIRE_TEMPERATURE,airSensorProxy,FIRE_AIR,[fireEvent])

updateCloudtimeObserver = TimeObserver([updateCloudEvent])

# Add Observers
temperatureSensorProxy.addObserver(lowHighTemperatureObserver)
temperatureSensorProxy.addObserver(fireObserver)

airSensorProxy.addObserver(fireObserver)
airSensorProxy.addObserver(highAirObserver)

soundSensorProxy.addObserver(highSoundObserver)

lightSensorProxy.addObserver(highLightObserver)

buttonSensorProxy.addObserver(buttonPressedObserver)

timeSensorProxy.addObserver(updateCloudtimeObserver)

##############################################
#Start Sub-systems
##############################################
temperatureSensorProxy.start()
lightSensorProxy.start()
soundSensorProxy.start()
airSensorProxy.start()
buttonSensorProxy.start()
timeSensorProxy.start()
lcdDisplay.start()