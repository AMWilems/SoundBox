# =====================================================
# Author: Alexander Wilems
# Main usage for controlling the interaction between user with Interface
# and software needed to control software for music playing

# =====================================================

from gpiozero import Button  # imports object of button
from mfrc522 import SimpleMFRC522
import RFID_Functions as RFID  # imports RFID_Functions file to allow read/write
                               # function from placeholder buttons
import LCD_Controller as LCD
import Spotify_Controller as Spotify
from RFID_Functions import Read
from signal import pause
from time import sleep

link = "4cOdK2wGLETKBW3PvgPWqT?si=5567b001dd3b495f"  # holds link set on RFID card

button_1 = Button(6)  # creation of button object to map
button_2 = Button(26)  # respective GPIO ports to input singal in boolean form
button_3 = Button(13)
button_4 = Button(19)
button_5 = Button(12)
button_6 = Button(16)

reader = SimpleMFRC522()

# =====================================================
# Last song to be completed on press of button 1
# =====================================================
def Last_Song_Controller():
    LCD.Last_Song_Message()
    Spotify.Previous()
    

# =====================================================
# play to be completed on press of button 2
# =====================================================
def Play_Controller():
    LCD.Play_Message()
    Spotify.Play(link)
    

# =====================================================
# pause to be completed on press of button 3
# =====================================================
def Pause_Controller():
    LCD.Pause_Message()
    Spotify.Pause()
    


# =====================================================
# next song to be completed on press of button 4
# =====================================================
def Next_Song_Controller():
    LCD.Next_Song_Message()
    Spotify.Next()
    
    
# =====================================================
# read card function call. takes no input
# assigns data gathered from RFID card, and set
# variable link to string contents
# =====================================================
def Read_Card_Controller():
    LCD.Read_Card_Message()
    link = RFID.Read()  # calls read function from RFID_Functions.py
                        # Sets string variable link to data read from RFID card

# =====================================================
# Write card function call. takes no input
# returns no variable
# currently used for dev only as final product
# does not have screen at current time
# =====================================================
def Write_Card_Controller():
    LCD.Write_To_Card_Messages()
    RFID.Write_Text()  # calls write function from RFID_Functions.py


# =====================================================
# On action functions for button presses. when button_n
# is pressed, calls the appropriate function to complete
# the respective function
# =====================================================
LCD.lcd.lcd_clear()
button_1.when_pressed = Last_Song_Controller
button_2.when_pressed = Play_Controller
button_3.when_pressed = Pause_Controller
button_4.when_pressed = Next_Song_Controller
button_5.when_pressed = Read_Card_Controller
button_6.when_pressed = Write_Card_Controller


pause()  # Tells the program to wait for an action to happen
# then continue the program without ending
