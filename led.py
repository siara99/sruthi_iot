import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #set board mode to broadcom
GPIO.setup(18,GPIO.OUT) #set up pin 18
GPIO.setup(15,GPIO.OUT)

while True:
    GPIO.output(18,1) #turn on pin 18
    GPIO.output(15,1)
    print('led on')
    print('led1 on')
    time.sleep(1) #delay for 1 sec
    GPIO.output(18,0) #turn offpin 18
    GPIO.output(15,0)
    print('led is off')
    print('led2 is off')
    time.sleep(2)
