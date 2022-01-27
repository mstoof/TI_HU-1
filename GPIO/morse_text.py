import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO morse text" )
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'.......'}

def pulse( pin_nr, high_time, low_time ):
   """
   Geef een puls op de pin:
   Maak de pin pin_nr hoog, wcht high_time,
   maak de pin laag, en wacht nog low_time
   # copieer hier je pulse implementatie
   """
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

def morse_text( pin_nr, dot_length, text ):
   """
   Laat de string s horen als morse code.
   De pin_nr is de pin die gebruikt wordt.
   De text mag de volgende characters bevatten: lowercase letters, spatie.
   De dot_length is de lengte van een punt (dot).
   De lengte van de andere characters wordt daar van afgeleid.
   """
   print(f'Original: {text}')
   text_morse = ""
   for char in text:
       char = char.upper()
       character = MORSE_CODE_DICT[char]
       text_morse += character
   print(text_morse)
   morse( pin_nr, dot_length, text_morse)


led = 18
GPIO.setup( led, GPIO.OUT )
morse_text( led, 0.2, "Hello world" )
