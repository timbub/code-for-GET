import RPi.GPIO as GPIO
import time

dec = [8, 11,7,1,0,5,12,6]
number = [1,0,0,0,0,0,0,0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dec, GPIO.OUT)
GPIO.output(dec, number)

time.sleep(10)

GPIO.output(dec, 0) 
GPIO.cleanup()
