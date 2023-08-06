#!/usr/bin/env python
from time import sleep
import subprocess
import os
import schedule

def reboot():
    os.system("reboot")

def showSlides():
    os.system("killall chromium-browser-v7; (chromium-browser --kiosk --app='xxxxx') > /dev/null 2>&1&")

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
