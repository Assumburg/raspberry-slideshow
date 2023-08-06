### Requirements
- A "mini" computer. (*I used a raspberry pi 3*)
- Linux operating system (*I used raspbian* OS)
- A google account

### Explanation
Ada asked me to provide a guide on how to setup the slideshow that we have at our club. We basically have a raspberry pi behind the tv run a slideshow that we make on google slides (as this can be shared online easily). The tv is set to a mode where after 3 hours it will turn itself off and that on a new HDMI signal detected, it will turn itself on. This is why in the attached  python code the raspberry pi will reboot on the opening times of our club, this will then cause the tv to turn on and as a bonus the slideshow will be updated to the latest version.

## Google slideshow
- Go to [google.com](google.com)
- Login to your account
- Click the 9 dotted menu item at the top right
- Go to slides/presentations
- Create a new slideshow
- Change the slideshow with whatever you want to show to the people

- Go to file/bestand > Share/delen > Publish on the internet - _Because the raspberry pi needs to load the slides remotely, it needs to be published on the internet. This also means that anyone in the world could view this slideshow (if they get a hold of the link). So make sure there is no personal data on the slides_
- Set the timer for how long a slide needs to be shown (we used 15 seconds)
- Check the boxes for "start on load" and "restart on last slide"
- Hit publish
- Keep the page with the link open

## On the Raspberry Pi
### Change configuration
- Open the "start" menu > Preferences > Raspberry Pi Configuration
- Go to the display tab
- Uncheck screen blanking
- Close the configuration window

### Run commands
- Open the terminal
- `sudo apt update && sudo apt upgrade -y`
- `sudo apt install unclutter`
- `sudo python3 -m pip install schedule`

### Files
`{ACCOUNTNAME}` _needs to be substituted with the account name that you set for your raspbian install._
_if you are not sure what the account name is, use the command:_ `whoami` (default is 'pi')

#### Python code
[[slides.py]] needs to be copied to the **/home/{ACCOUNTNAME}/** folder.
_if you are going to use the gpio pins to add buttons for extra functionality, look at [[clubSlides.py]]. This file is used at our club to show members their personal best scores and if they are allowed to shoot at a certain distance. This involves a different slideshow, that does not loop/autostart and where the slide id is injected at the end of the link depending on which button is pressed to only show that specific slide_

In the code file you will have to change the URL to the link that you can copy from the google webpage.
- Copy the link from the google webpage
- Replace the xxxxx in the python code with the clipboard content

#### Create
**/etc/xdg/autostart/slides.desktop** (this file will start the slide show on startup)
```
[Desktop Entry]
Name=Slides
Exec=/usr/bin/python3 /home/{ACCOUNTNAME}/slides.py
```

#### Edit
**/home/{ACCOUNTNAME}/.config/lxsession/LXDE-pi/desktop.conf**
Add `@unclutter -idle 0.5` at the bottom of the file
_this command hides the mouse pointer after 0.5 seconds of inactivity_

### Small test
Run the command `/usr/bin/python3 /home/{ACCOUNTNAME}/slides.py` or `/usr/bin/python3 /home/{ACCOUNTNAME}/clubSlides.py` depending on what file you used (_wait up to 10 seconds_)
There should not be any error, but otherwise you might have to fix whatever pops up.

### Final command
`sudo reboot`

Now it should automagically start the slideshow on startup
If it does not work. Ada will have an email address to ask any questions.

Have fun!
