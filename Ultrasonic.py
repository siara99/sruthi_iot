import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

TRIG = 23
ECHO = 24

print ("Distance Mesurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print ("Waiting for Sensor Data")

while True:
    
    GPIO.output(TRIG, False)
    
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()


    pulse_duration = pulse_end - pulse_start

    # 34300=Distance/Time/2,    17150=Distance/Time,   17150 X Time = Distance (cm)

    distance = pulse_duration * 17150
    distance = round(distance,0)

    if distance > 2 and distance < 150: 
        print ("Distance:",distance,"cm")
        GPIO.output(25,1)
    else:
        print ("Out of Range")
        GPIO.output(25,0)

