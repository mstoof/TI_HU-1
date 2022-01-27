import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "sr04 print" )

sr04_trig = 20
sr04_echo = 21

GPIO.setup( sr04_trig, GPIO.OUT )
GPIO.setup( sr04_echo, GPIO.IN)

def sr04( trig_pin, echo_pin ):
   """
   Return the distance in cm as measured by an SR04
   that is connected to the trig_pin and the echo_pin.
   These pins must have been configured as output and input.s
   """
    
   # send trigger pulse    
   GPIO.output(trig_pin, False)
   time.sleep(2)
   GPIO.output(trig_pin, True)
   start_time = time.time()
   stop_time = time.time()
   print("program is starting")
   time.sleep(0.00001)
   GPIO.output(trig_pin, False)
   
   # wait for echo high and remember its start time
   while GPIO.input(echo_pin) == 0:
       print("still in start_time")
       start_time = time.time()
        
   # wait for echo low and remember its end time
   while GPIO.input(echo_pin) == 1:
       print("still in end_time")
       stop_time = time.time()

   # calculate and return distance
   time_elapsed = stop_time - start_time

   distance = (time_elapsed * 34300) / 2
   print(f"distance is: {distance}")
   return distance

while True:
   print( sr04( sr04_trig, sr04_echo ))
   time.sleep(0.5)

