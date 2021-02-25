import random
import picodisplay as display 
import time, _thread, machine
from machine import Timer

tim = Timer()

width = display.get_width()
height = display.get_height()+10 #hack

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display.init(display_buffer)

display.set_backlight(1.0)

display.set_pen(255, 255, 255)        
display.clear()

radius=2
s = 60000

def tick(timer):
    global display
    display.update()

tim.init(period=200, mode=Timer.PERIODIC, callback=tick)


def task(s, radius, pen):
    global display
#    print(pen)
    for i in range(1,s):
        display.set_pen(pen)        
        display.rectangle(random.randint(0,width-1), random.randint(0,height-1), radius, radius)

#_thread.start_new_thread(task, (0.2, 10))

pen_red   = display.create_pen(250, 0, 0)
pen_green = display.create_pen(0, 250, 0)
pen_blue = display.create_pen(0, 0, 250)

tic = time.ticks_ms()
task(s,radius, pen_red)
display.update()
toc = time.ticks_ms()
print("Time: ",(toc - tic)/1000.0)

time.sleep(2)

tic = time.ticks_ms()
_thread.start_new_thread(task, (s/2,radius, pen_green))
task(s/2,radius, pen_green)
display.update()
toc = time.ticks_ms()
print("Time: ",(toc - tic)/1000.0)
tim.deinit()