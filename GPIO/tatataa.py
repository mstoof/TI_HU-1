import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO tatata" )

def tatata( pin_nr, high_time, low_time ):
   """
   Geef een puls op de pin:
   Maak de pin pin_nr hoog, wacht high_time,
   maak de pin laag, en wacht nog low_time
   """
   for i in range(3):
       GPIO.output(pin_nr, GPIO.HIGH)
       time.sleep(low_time)
       GPIO.output(pin_nr, GPIO.LOW)
       time.sleep(low_time)
   time.sleep(high_time)
   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(high_time)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(high_time)

led = 18
GPIO.setup( led, GPIO.OUT )
while True:
   tatata( led, 0.5, 0.2 )
