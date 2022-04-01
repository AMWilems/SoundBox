#=====================================================
#Author: Alexander Wilems
#LCD screen control to provide the user info on 
#=====================================================
from time import sleep
import I2C_LCD_driver

lcd = I2C_LCD_driver.lcd()

def Display_Song_Info():
    
def Play_Message():
    lcd.lcd_display_string("Playing...",1,2)

def Pause_Message():
    lcd.lcd_display_string("Pausing...",1,2)

def Next_Song_Message():
    lcd.lcd_display_string("Next Song...",1,0)

def Last_Song_Message():
    lcd.lcd_display_string("Last Song...",1,0)

def Scan_Card_Message():
    lcd.lcd_display_string("Please Scan",1,0)
    lcd.lcd_display_string("Card Now"2,0)

def Write_Card():
    lcd.lcd_display_string("
def Clear_Screen():
    lcd.lcd_clear()
