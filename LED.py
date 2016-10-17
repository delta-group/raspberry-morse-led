import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

# my message to raspberry
raspString = "hi pi" 
raspMessage = raspString.split()

# my message to the world
myString = "hello world"
myMessage = myString.split()

# our message to little manger baby raspberry
print raspMessage
for word in raspMessage:
    morseWord = to_morse(str(word))
    print morseWord
    for char in morseWord:
        if char == '.':
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.25) # short green light for dot
            GPIO.output(17,GPIO.LOW)
            time.sleep(.1) # pause between dots/dashes
        if char == "-":
            GPIO.output(17,GPIO.HIGH)
            time.sleep(.65) # long green light for dash
            GPIO.output(17,GPIO.LOW)
            time.sleep(.1)  # pause between dots/dashes
        time.sleep(.2)     # pause after character  
    time.sleep(.4)          # pause between words

# raspberry's awakening
print myMessage
for word in myMessage:
    morseWord = to_morse(str(word))
    print morseWord
    for char in morseWord:
        if char == '.':
            GPIO.output(18,GPIO.HIGH)
            time.sleep(.25) # short red light for dot
            GPIO.output(18,GPIO.LOW)
            time.sleep(.1) # pause between dots/dashes
        if char == "-":
            GPIO.output(18,GPIO.HIGH)
            time.sleep(.65) # long red light for dash
            GPIO.output(18,GPIO.LOW)
            time.sleep(.1)  # pause between dots/dashes
        time.sleep(.2)     # pause after character  
    time.sleep(.4)          # pause between words
