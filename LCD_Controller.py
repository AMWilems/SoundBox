#=====================================================
#Author: Alexander Wilems
#LCD screen control to provide the user info on 
#=====================================================
from time import sleep
import I2C_LCD_driver

lcd = I2C_LCD_driver.lcd()

def Play_Message():
    lcd.lcd_clear()
    lcd.lcd_display_string("Playing...",1,2)

def Pause_Message():
    lcd.lcd_clear()
    lcd.lcd_display_string("Pausing...",1,2)
    Wait_And_Clear()

def Next_Song_Message():
    lcd.lcd_clear()
    lcd.lcd_display_string("Next Song...",1,0)
    Wait_And_Clear()

def Last_Song_Message():
    lcd.lcd_clear()
    lcd.lcd_display_string("Last Song...",1,0)
    Wait_And_Clear()

def Read_Card_Message():
    lcd.lcd_clear()
    lcd.lcd_display_string("Please Scan",1,0)
    lcd.lcd_display_string("Card Now",2,0)

def New_Data():
    lcd.lcd_clear()
    lcd.lcd_display_string("Please input",1,0)
    lcd.lcd_display_string("new data. ^.^ ",2,0)
    
def Write_To_Card_Messages():
    lcd.lcd_clear()
    lcd.lcd_display_string("Place tag",1,0)
    lcd.lcd_display_string("on pad",2,0)

def Successful():
    lcd.lcd_clear()
    lcd.lcd_display_string("Written",1,0)
    lcd.lcd_display_string("Successfully",2,0)
    Wait_And_Clear()
    

def Card_Contents(card_data):
    lcd.lcd_clear()
    lcd.lcd_display_string(card_data,1,0)
    Wait_And_Clear()

def Wait_And_Clear():
    sleep(3)
    lcd.lcd_clear()
    
