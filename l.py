import RPi.GPIO as GPIO
import dht11
import time
#Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#read data using pin 14
instance = dht11.DHT11(pin = 14)

while True:
    result = instance.read()
    if result.is_valid():

         print "Temeprature: %d C" % result.temperature,"Humidity: %d %%" % result.humidity

    time.sleep(5)
