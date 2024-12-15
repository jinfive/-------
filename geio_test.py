import RPi.GPIO as GPIO
import time

switch1=6
switch2=19
switch3=20
led1=13
led2=26
led3=21
rel1=14
rel2=15
rel3=18
GPIO.setmode(GPIO.BCM)
GPIO.setup([switch1,switch2,switch3],GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(4,GPIO.IN)
GPIO.setup([led1,led2,led3,rel1,rel2,rel3],GPIO.OUT)
count=0
#GPIO.output(4, GPIO.HIGH)

vib=0
try:
    while True:
        if not GPIO.input(switch1):
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(rel1, GPIO.HIGH)
        else :
            GPIO.output(rel1, GPIO.LOW)
            GPIO.output(led1, GPIO.LOW)

        if not GPIO.input(switch2):
            GPIO.output(led2, GPIO.HIGH)
            GPIO.output(rel2, GPIO.HIGH)
        else :
            GPIO.output(rel2, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)

        if not GPIO.input(switch3):
            GPIO.output(led3, GPIO.HIGH)
            GPIO.output(rel3, GPIO.HIGH)
        else :
            GPIO.output(led3, GPIO.LOW)
            GPIO.output(rel3, GPIO.LOW)
except Exception as e:
    GPIO.cleanup()