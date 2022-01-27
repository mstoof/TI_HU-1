import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "input copy" )

led = 18
switch = 23

GPIO.setup( led, GPIO.OUT )
GPIO.setup( switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
while True:
   time.sleep(0.50)
   
   if( GPIO.input( switch )) == 0:
       lights = 'lights on' if GPIO.input(led) == GPIO.LOW else 'lights off'
       print(f'button pressed, {lights}')
       if GPIO.input(led) == GPIO.LOW:
           GPIO.output( led, GPIO.HIGH)
       else:
           GPIO.output( led, GPIO.LOW)
   time.sleep( 0.1 )


