import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO=24
print ("Distance mesurement in progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
print ("waiting for sensor data")
while True:
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()


    pulse_duration=pulse_end-pulse_start

    distance=pulse_duration*17150
    distance=round(distance,0)
    if distance>2 and distance<150:
        print ("Distance:",distance,"cm")
        GPIO.output(14,1)
    else:
        print ("out of range")
        GPIO.output(14,0)
