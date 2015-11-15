import time
import pyupm_mic as upmMicrophone 

# Attach microphone to analog port A0
myMic = upmMicrophone.Microphone(2)
threshContext = upmMicrophone.thresholdContext()
threshContext.averageReading = 0
threshContext.runningAverage = 0
threshContext.averagedOver = 2

# Infinite loop, ends when script is cancelled
# Repeatedly, take a sample every 2 microseconds;
# find the average of 128 samples; and
# print a running graph of dots as averages
while(1):
    buffer = upmMicrophone.uint16Array(128)
    len = myMic.getSampledWindow(2, 128, buffer);
    if len:
        thresh = myMic.findThreshold(threshContext, 30, buffer, len)
        myMic.printGraph(threshContext)
        if(thresh):
            print "Threshold is ", thresh
            print "Value is", myMic.value()

# Delete the upmMicrophone object
del myMic