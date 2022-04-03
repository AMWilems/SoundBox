#=====================================================
#Author: Alexander Wilems
#script to provide functionality for RFID reader
#allowing data capture from reading
#and create data by writing
#=====================================================

import RPi.GPIO as GPIO             #imports gpio controls to work with
                                    #Rasberry pi pin numbering convention
from mfrc522 import SimpleMFRC522   #Imports library for RFID basic functions
                                    #on hw level
import LCD_Controller as LCD

GPIO.setwarnings(False)             #disables warning from hw as RFID reader
                                    #throws warning of already in use
                                    #and that information is not needed in logs

reader = SimpleMFRC522()            #creates instance of reader to take data from RFID
id = "ERROR: Read unsuccessful"     #placeholder for if card is not read, displays error to log 
text = "ERROR: Read unsuccessful"   #placeholder for if card is not read, displays error to log 

#=====================================================
#function to read data on RFID device and text return
#to main script to be used in playing media after scan
#automatically
#takes none, returns string
#=====================================================
def Read():
    
    try:                            #while loop that keeps running until action inside is completed
        id, text = reader.read()    #read RFID card, gather card ID and text
    finally:                        #after try has completed, returns string text
        LCD.Clear_Screen()
        LCD.Card_Contents(text)
        return text 
        
    
#=====================================================
#function used to write data to RFID reader, then
#display that the function has completed
#used in dev only at the moment as keyboard is required
#takes none returns none 
#=====================================================
def Write_Text():
    try:                            
        text = input('New data:')   #asks user to enter information needed on the card for
                                    #new playlist to be set to play
        reader.write(text)          #waits for RFID to be detected before writing data to RFID card
        
    finally:
        LCD.Clear_Screen()
        LCD.Successful()
