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

from RFID_Functions import Read
from signal import pause
from time import sleep

link = ""  # holds link set on RFID card

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
def Call_Function_1():
    LCD.Clear_Screen()
    LCD.Last_Song_Message()

# =====================================================
# play to be completed on press of button 2
# =====================================================
def Call_Function_2():
    LCD.Clear_Screen()
    LCD.Play_Message()

# =====================================================
# pause to be completed on press of button 3
# =====================================================
def Call_Function_3():
    LCD.Clear_Screen()
    LCD.Pause_Message()


# =====================================================
# next song to be completed on press of button 4
# =====================================================
def Call_Function_4():
    LCD.Clear_Screen()
    LCD.Next_Song_Message()
    
# =====================================================
# read card function call. takes no input
# assigns data gathered from RFID card, and set
# variable link to string contents
# =====================================================
def Call_Function_5():
    LCD.Clear_Screen()
    LCD.Read_Card_Message()
    print("scan card now\n")
    link = RFID.Read()  # calls read function from RFID_Functions.py
    # Sets string variable link to data read from RFID card
    print("Card Contents: ", link, "\n")


# =====================================================
# Write card function call. takes no input
# returns no variable
# currently used for dev only as final product
# does not have screen at current time
# =====================================================
def Call_Function_6():
    LCD.Clear_Screen()
    LCD.Write_To_Card_Messages()
    RFID.Write_Text()  # calls write function from RFID_Functions.py


# =====================================================
# On action functions for button presses. when button_n
# is pressed, calls the appropriate function to complete
# the respective function
# =====================================================

button_1.when_pressed = Call_Function_1
button_2.when_pressed = Call_Function_2
button_3.when_pressed = Call_Function_3
button_4.when_pressed = Call_Function_4
button_5.when_pressed = Call_Function_5
button_6.when_pressed = Call_Function_6

pause()  # Tells the program to wait for an action to happen
# then continue the program without ending
