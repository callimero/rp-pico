# Quick and dirty Mandelbrot calculation

import time, random
import picodisplay as display 

width = display.get_width()
height = display.get_height()+10

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display.init(display_buffer)

display.set_backlight(1.0)

# Plot window
RE_START = -2.6
RE_END = 1.6
IM_START = -1.2
IM_END = 1.6

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


display.set_pen(255, 255, 255)        
display.clear()
display.update()

# calculates some resolutions and refines (stupidly)
step = 8
MAX_ITER = 64

for step in range(8,0,-1):
    for x in range(0, width-1,step):
        for y in range(0, height-1,step):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / width) * (RE_END - RE_START),
                        IM_START + (y / height) * (IM_END - IM_START))
            # Compute the number of iterations
            m = mandelbrot(c)
            color = 255 - int(m * 255 / MAX_ITER)
            display.set_pen(color,color,color)
            display.rectangle(x, y,step,step)
        display.update()
