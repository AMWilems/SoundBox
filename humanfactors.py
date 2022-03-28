#=====================================================
#Author: Alexander Wilems
#=====================================================

from gpiozero import Button
import RFID_Functions as RFID
from signal import pause

link = ""

button_1 = Button(6)
button_2 = Button(26)
button_3 = Button(13)
button_4 = Button(19)
button_5 = Button(12)
button_6 = Button(16)

def Call_Function_1():
    print ("button 1 pressed\n")
    
def Call_Function_2():
    print ("button 2 pressed\n")
    
def Call_Function_3():
    print ("button 3 pressed\n")
    
def Call_Function_4():
    print ("button 4 pressed\n")
    
def Call_Function_5():
    print("scan card now\n")
    link = RFID.Read()
    print ("Card Contents: ", link, "\n")
    
def Call_Function_6():
    RFID.Write_Text()
    print ("card text write function completed\n")
           
button_1.when_pressed = Call_Function_1
button_2.when_pressed = Call_Function_2
button_3.when_pressed = Call_Function_3
button_4.when_pressed = Call_Function_4
button_5.when_pressed = Call_Function_5
button_6.when_pressed = Call_Function_6

pause()

        
