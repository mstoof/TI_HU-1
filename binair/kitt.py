import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "binair walk" )

led_pins = [ 5, 6, 13, 19, 26 ]

for gpio in led_pins:
   GPIO.setup( gpio, GPIO.OUT )

def leds( pins, value, delay ):
    for gpio in pins:
        if value % 2 == 1:
           GPIO.output( gpio, GPIO.HIGH )
        else:
           GPIO.output( gpio, GPIO.LOW )
        value = value // 2
    time.sleep( delay )

delay = 0.2
try: 
    while True:
        time.sleep(delay)
        for led in led_pins:
            leds( led_pins, led, delay )
    
        for led in reversed(led_pins):
            leds( led_pins, led, delay )

except:
    for led in led_pins:
        GPIO.output( led, GPIO.LOW)
