import RPi.GPIO as GPIO
import time

servoPin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

p = GPIO.PWM(servoPin, 50)
p.start(2.5)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPin, True)
    p.ChangeDutyCycle(duty)
    time.sleep(0.2)
    GPIO.output(servoPin, False)
    p.ChangeDutyCycle(0)


while True:
    ranges = [0, 90, 180]
    for a in ranges:
        SetAngle(a)
    for a in reversed(ranges):
        SetAngle(a)
     

