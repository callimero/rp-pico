# Pi nach Monte-Carlo Methode bestimmen
# caw@make-magazin.de, 2021-03-14

import math
import random
 
import picodisplay as display # Picodisplay!

width = display.get_width()
height = display.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display.init(display_buffer)

display.set_backlight(1.0)
display.set_pen(255, 255, 255)        
display.clear()
display.update()


# Test eines Punktes
def one_sample():
    y, x = random.random(), random.random()   
    if math.pow(y,2) + math.pow(x,2) <= 1.0:
        display.set_pen(0, 255, 0)        
        display.pixel(int(x*height), int(y*height))
        return 1
    else:
        display.set_pen(255, 0, 0)        
        display.pixel(int(x*height), int(y*height))
        return 0
    
    
display.set_pen(0, 0, 200)
display.text("Happy Pi-Day!",140,90, 100, 3)

runs = 100 #wieviele Iterationen zwischen Screen Refresh
iterations = 100000 # Durchläufe

pi = 0.0
for it in range(1,iterations):
    for i in range(runs):
        pi += one_sample()
    # Text Info
    display.set_pen(255, 255, 255)        
    display.rectangle(140,10,120,46)
    display.set_pen(0, 0, 200)
    display.text("Pi: "+str(pi*4.0/runs/it),140,10, 200, 2)               # Pi
    display.text("It: "+str(runs*it),140,26, 200, 2)                      # Iterationen
    display.text("Fe: "+str((pi*4.0/runs/it-math.pi)*100),140,42, 200, 2) # Fehler %
    display.update()
