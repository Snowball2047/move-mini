from microbit import *
import radio
channel = 1

def button():
    buttonNum = 0
    buttonNum = pin2.read_analog()
    if buttonNum < 256:
        return 1
    elif buttonNum < 597:
        return 2
    elif buttonNum < 725:
        return 3
    elif buttonNum < 793:
        return 4
    elif buttonNum < 836:
        return 5
    elif buttonNum < 938:
        return 6
    else:
        return 0

radio.on()
radio.config(channel=channel)
while True:
    buttonNum = str(button())
    if buttonNum == None:
        buttonNum = 0
    joyx = 0
    joyy = 0
    joyx = pin0.read_analog()
    joyy = pin1.read_analog()
    if joyx < 400:
        buttonNum += '1'
    elif joyx > 600:
        buttonNum += '2'
    elif joyy < 400:
        buttonNum += '3'
    elif joyy > 600:
        buttonNum += '4'
    else:
        buttonNum += '0'
    radio.send(buttonNum)
