import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse code" )

def pulse( pin_nr, high_time, low_time):
    
   GPIO.output(pin_nr, GPIO.HIGH)
   time.sleep(high_time)
   GPIO.output(pin_nr, GPIO.LOW)
   time.sleep(low_time)

def morse( pin_nr, dot_length, text ):
   """
   Laat de text horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: spatie, streepje, punt.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """
   for char in text: 
       if char == ".":
           GPIO.output( pin_nr, GPIO.HIGH)
           time.sleep(dot_length)
       elif char == "-":
           GPIO.output( pin_nr, GPIO.HIGH)
           time.sleep(dot_length * 2.5)
       else:
           GPIO.output( pin_nr, GPIO.HIGH)
           time.sleep(dot_length * 5)
       GPIO.output( pin_nr, GPIO.LOW)
       time.sleep(0.5)

led = 18
GPIO.setup( led, GPIO.OUT )
morse( 18, 0.2, ".--. -.-- - .... --- -." )
