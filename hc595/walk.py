import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "hc595 walk" )

shift_clock_pin = 5
latch_clock_pin = 6
data_pin = 13

GPIO.setup( shift_clock_pin, GPIO.OUT )
GPIO.setup( latch_clock_pin, GPIO.OUT )
GPIO.setup( data_pin, GPIO.OUT )
GPIO.output(data_pin, 00000000)

def hc595( shift_clock_pin, latch_clock_pin, data_pin, value, delay ):
   # implementeer deze functie
   binary = f'{value:08b}'

   for i in range(8):
       print(binary)
       GPIO.output(data_pin, int(binary))
       time.sleep(delay)
       GPIO.output(shift_clock_pin, 1)
       GPIO.output(shift_clock_pin, 0)
       time.sleep(delay)
       
       GPIO.output(latch_clock_pin, 1)
       GPIO.output(latch_clock_pin, 0)

delay = 0.1
while True:
   hc595( shift_clock_pin, latch_clock_pin, data_pin,   1, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin,   2, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin,   4, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin,   8, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin,  16, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin,  32, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin,  64, delay )
   hc595( shift_clock_pin, latch_clock_pin, data_pin, 128, delay )

