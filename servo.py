import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,50)
p.start(7.5)
try:
    while True:
        p.ChangeDutyCycle(7.5)
        time.sleep(2)
        print("Servo Rotates 90A C")
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        print("Servo Rotates 180A C")
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
        print("Servo Rotates 0A C");

except KeyboardInterrupt:
    p.stop()
        
