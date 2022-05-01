from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

Redled = LED(18)
Blueled = LED(24)
Greenled = LED(23)

root = Tk()
root.title("GUI LED")
myFont = tkinter.font.Font(family = 'Helvetica', size = 20, weight = 'bold')

def RedledToggler():
	if Redled.is_lit:
		Redled.off()
		RedLedToggleButton["text"] = " Red LED ON"
	else:
		Redled.on()
		RedLedToggleButton["text"] = " Red LED Off"
		
		Blueled.off()
		BlueLedToggleButton["text"] = " Blue LED On"
		
		Greenled.off()
		GreenLedToggleButton["text"] = " Green LED On"
		
def BlueledToggler():
	if Blueled.is_lit:
		Blueled.off()
		BlueLedToggleButton["text"] = "Turn Blue LED ON"
	else:
		Blueled.on()
		BlueLedToggleButton["text"] = "Turn Blue LED Off"
		
		Redled.off()
		RedLedToggleButton["text"] = "Turn Red LED On"
		
		Greenled.off()
		GreenLedToggleButton["text"] = "Turn Green LED On"
		
def GreenledToggler():
	if Greenled.is_lit:
		Greenled.off()
		GreenLedToggleButton["text"] = "Turn Green LED ON"
	else:
		Greenled.on()
		GreenLedToggleButton["text"] = "Turn Green LED Off"
		
		Redled.off()
		RedLedToggleButton["text"] = "Turn Red LED On"
		
		Blueled.off()
		BlueLedToggleButton["text"] = "Turn Blue LED On"
		
def quitGUI():
	RPi.GPIO.cleanup
	root.destroy()
	
RedLedToggleButton = Button(root, text = 'Turn Red LED On', font = myFont, command = RedledToggler, bg = 'Red', height = 1, width =50)
RedLedToggleButton.grid(row=0, column=1)

BlueLedToggleButton = Button(root, text = 'Turn Blue LED On', font = myFont, command = BlueledToggler, bg = 'Blue', height = 1, width =50)
BlueLedToggleButton.grid(row=1, column=1)

GreenLedToggleButton = Button(root, text = 'Turn Green LED On', font = myFont, command = GreenledToggler, bg = 'Green', height = 1, width =50)
GreenLedToggleButton.grid(row=2, column=1)

ExitButton = Button(root, text = 'Exit', font = myFont, command = quitGUI, bg = 'Gray', height = 1, width = 50)
ExitButton.grid(row=3, column=1)
root.mainloop()
