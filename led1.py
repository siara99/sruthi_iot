import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()#set GPIO to default

import time
#blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(.5)
    return
#to use Raspberry pi board pin numbers
GPIO.setmode(GPIO.BCM)
#set up GPIO output channel
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
#blink GPIO17 50 times
for i in range(0,5):
    blink(11)
    blink(13)
    blink(15)
    blink(19)
GPIO.cleanup()

    
