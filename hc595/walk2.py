import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print( "HC595 walk" )

shift_clock_pin = 5
latch_clock_pin = 6
data_pin = 13

GPIO.setup( shift_clock_pin, GPIO.OUT)
GPIO.setup( latch_clock_pin, GPIO.OUT)
GPIO.setup( data_pin, GPIO.OUT)


def hc595( shift_clock_pin, latch_clock_pin, data_pin, value, delay):
    GPIO.output(shift_clock_pin, 0)
    GPIO.output(latch_clock_pin, 0)
    GPIO.output(shift_clock_pin, 1)

    binary = f'{value:08b}'
    
    for i in range(7, -1, -1):
        print(i)
        GPIO.output(shift_clock_pin, 0)
        GPIO.output(data_pin, int(binary[i]))
        GPIO.output(shift_clock_pin, 1)
        time.sleep(delay) 

    GPIO.output(shift_clock_pin, 0)
    GPIO.output(latch_clock_pin, 1)
    GPIO.output(shift_clock_pin, 1)

if __name__ == '__main__':
    try:
        while True:
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 1,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 2,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 4,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 8,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 16,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 32,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 64,  0.2)
            hc595(shift_clock_pin, latch_clock_pin, data_pin, 128,  0.2)
    except:
        GPIO.cleanup()
        # shutdown all lights
        GPIO.output(shift_clock_pin, 0)
        GPIO.output(latch_clock_pin, 0)
        GPIO.output(shift_clock_pin, 1)
        GPIO.output(shift_clock_pin, 0)
GPIO.output(data_pin, 00000000)
GPIO.output(shift_clock_pin, 1)
GPIO.output(shift_clock_pin, 0)
GPIO.output(latch_clock_pin, 1)
GPIO.output(shift_clock_pin, 1)
# end default 
