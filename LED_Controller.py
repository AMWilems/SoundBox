#=====================================================
#Author: Alexander Wilems
#=====================================================

from gpiozero import LED    #Imports LED control function from gpiozero
from time import sleep      #calls in sleep function to have program wait
                            
flash_time = 0.15           #Variable sets the time in seconds the system will wait before turning the LED back off
LED_location = 22           #Variable for GPIO channel location of LED
led = LED(LED_location)     #creates an instance of LED, sets LED_location as pin to get data from 

#=====================================================
#Function to turn light on and backl off quickly to
#represent acknowledgement of user input
#=====================================================
def Flash_LED():
    led.on()                #Turns LED on
    sleep(flash_time)       #wait defined amount of time
    led.off()               #turn LED back off
