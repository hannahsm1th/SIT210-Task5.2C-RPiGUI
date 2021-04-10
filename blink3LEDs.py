from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

## Hardware
led1 = LED(14)
led2 = LED(23)
led3 = LED(25)

## GUI
win = Tk()
win.title("Three LEDs")
buttonFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "normal")

## Program Functions
def led1Toggle():
        if led1.is_lit:
                led1.off()
                led1Button["text"] = "Turn on RED"
        else:
                led1.on()
                led2.off()
                led2Button["text"] = "Turn on BLUE"
                led3.off()
                led3Button["text"] = "Turn on YELLOW"
                led1Button["text"] = "Turn off RED"
                
def led2Toggle():
        if led2.is_lit:
                led2.off()
                led2Button["text"] = "Turn on BLUE"
        else:
                led2.on()
                led1.off()
                led1Button["text"] = "Turn on RED"
                led3.off()
                led3Button["text"] = "Turn on YELLOW"
                led2Button["text"] = "Turn off BLUE"

def led3Toggle():
        if led3.is_lit:
                led3.off()
                led3Button["text"] = "Turn on YELLOW"
        else:
                led3.on()
                led2.off()
                led2Button["text"] = "Turn on BLUE"
                led1.off()
                led1Button["text"] = "Turn on RED"
                led3Button["text"] = "Turn off YELLOW"

## Widgets

led1Button = Button(win, text = 'Turn on RED', font = buttonFont, command = led1Toggle, bg = 'bisque2', height = 1, width = 24)
led2Button = Button(win, text = 'Turn on BLUE', font = buttonFont, command = led2Toggle, bg = 'bisque2', height = 1, width = 24)
led3Button = Button(win, text = 'Turn on YELLOW', font = buttonFont, command = led3Toggle, bg = 'bisque2', height = 1, width = 24)
led1Button.grid(row=0,column=1)
led2Button.grid(row=0,column=2)
led3Button.grid(row=0,column=3)
