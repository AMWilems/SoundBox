import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

reader = SimpleMFRC522()
id = "ERROR: Read unsuccessful"
text = "ERROR: Read unsuccessful"

def Read():
    try:
        id, text = reader.read()
    finally:
       return text 
        
    

def Write_Text():
    try:
        text = input('New data:')
        print("Place tag on pad")
        reader.write(text)
        
    finally:
        print("Written")
