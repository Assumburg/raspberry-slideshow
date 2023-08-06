#!/usr/bin/env python
from time import sleep
from gpiozero import Button
import subprocess
from threading import Thread
import os
import schedule

recurve = Button(17)
compound = Button(23)
barebow = Button(24)

long_press_seconds = 2

def showSlide(klasse):
    os.system("killall chromium-browser-v7; (chromium-browser --kiosk --app='xxxxx#slide=id." + klasse + "') > /dev/null 2>&1&")    
    sleep(30)
    showSlides()
    sleep(5)

def reboot():
    os.system("reboot")

def recurveButton(state):
    sleep(long_press_seconds) #adjust to your liking
    act = state.is_active
    if act: # long press action here
        Thread(target = showSlide("g133ecd51b0c_0_23")).start()
    else: #short press action here
        Thread(target = showSlide("g33e5530376_0_50")).start()

def compoundButton(state):
    sleep(long_press_seconds) #adjust to your liking
    act = state.is_active
    if act: # long press action here
        Thread(target = showSlide("g123d08e8663_0_0")).start()
    else: #short press action here
        Thread(target = showSlide("g33e5530376_0_55")).start()

def barebowButton(state):
    sleep(long_press_seconds) #adjust to your liking
    act = state.is_active
    if act: # long press action here
        Thread(target = showSlide("g133ecd51b0c_0_35")).start()
    else: #short press action here
        Thread(target = showSlide("g33e5530376_0_45")).start()

def showSlides():
    os.system("killall chromium-browser-v7; (chromium-browser --kiosk --app='xxxxx') > /dev/null 2>&1&")

recurve.when_pressed = recurveButton
compound.when_pressed = compoundButton
barebow.when_pressed = barebowButton

schedule.every().monday.at("19:00").do(reboot)
schedule.every().wednesday.at("19:30").do(reboot)
schedule.every().friday.at("19:30").do(reboot)
#schedule.every().saturday.at("10:00").do(reboot)
schedule.every().sunday.at("12:00").do(reboot)

try:
    sleep(8)
    showSlides()
    while(True):
        schedule.run_pending()
        sleep(60)
except KeyboardInterrupt:
    print("Goodbye")
print("Loop ends here")
