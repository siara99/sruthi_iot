import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    input_state=GPIO.input(12)
    input_state1=GPIO.input(16)
    #if(input_state==1 and input_state1==1):
        #print("light is on1")
        #GPIO.output(18,1)
    #else:
        #print("light is off1")
        #GPIO.output(18,0)
    if(input_state1==0 and input_state==0):
        print("light is off")
        GPIO.output(18,0)
    else:
        print("light is on")
        GPIO.output(18,1)
     #time.sleep(5)   
