# Picodisplay demo Make Magazin 2021 (caw)
import time, random

# Boilerplate code which will be needed for any program using the Pimoroni Display Pack
# Import the module containing the display code
import picodisplay as display

def makemagazin():
    display.set_pen(makeRed)
    display.text("Make:", 10, 10, 64, 6)

    display.set_pen(makeBlue)
    #display.rectangle(20, 20, 40, 20)
    display.text("Deutschlands gefaehrlichstes DIY-Magazin", 10, 5, 240, 1)

    display.set_pen(makeGray)
    display.rectangle(5, 50, width-10, height-55)

    # update/push changes to display (to avoid flicker)

# 240x135
# Get the width of the display, in pixels
width = display.get_width()
# Get the height of the display, in pixels
height = display.get_height()

# Use the above to create a buffer for the screen.  It needs to be 2 bytes for every pixel.
display_buffer = bytearray(width * height * 2)

# Start the display!
display.init(display_buffer)
# Boilerplate end

# setting the backlight intensity
display.set_backlight(1.0)

# set drawing color
display.set_pen(255,255,255)

# define pens/colors
makeRed = display.create_pen(255, 0, 0)
makeBlue = display.create_pen(0, 0, 200)
makeGray = display.create_pen(220,220,220)

# "clear" (just fills display with color=
display.clear()

# update/push changes to display (to avoid flicker)
display.update()

makemagazin()

display.set_pen(makeRed)
while not(display.is_pressed(display.BUTTON_A)):
    display.pixel(random.randint(5, 234), random.randint(50, 129))
    if display.is_pressed(display.BUTTON_Y):
        display.set_pen(makeBlue)
        display.text("Pico", random.randint(5, 234), random.randint(50, 129), 100, 2)
        display.set_pen(makeRed)

        
    display.update()

# wait a second
time.sleep(1)
