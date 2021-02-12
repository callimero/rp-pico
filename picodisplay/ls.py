# # List directory for picodisplay, little gui
import time,os 
import picodisplay as display 

# setup display
width = display.get_width()
height = display.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display.init(display_buffer)
# setting the backlight intensity
display.set_backlight(1.0)

# Get all files
files = sorted(os.listdir(),key=str.lower)
print(files)

#clear
display.set_pen(255,255,255)
display.clear()

# "GUI"
display.set_pen(200,30,30)
display.text("Exit", 5,15, 230, 3)
display.set_pen(30,200,30)
display.text("Up", 200,15, 30, 3)
display.set_pen(30,30,200)
display.text("Start", 5,99, 230, 3)
display.set_pen(30,200,30)
display.text("Down", 164,99, 230, 3)
display.update()

p=0
while not(display.is_pressed(display.BUTTON_A)):
    display.set_pen(255,255,255)
    display.rectangle(0,40,240,60)
    
    if display.is_pressed(display.BUTTON_Y):
        p=p+1
        time.sleep(0.07)
        if p>len(files)-1:
            p=0
    if display.is_pressed(display.BUTTON_X):
       p=p-1
       time.sleep(0.07)
       if p<0:
           p=len(files)-1
    if display.is_pressed(display.BUTTON_B):
        __import__(files[p])
        exit(0)

    display.set_pen(230,0,20)
    display.text(files[p], 5,55, 230, 3)
    display.update()
    time.sleep(0.12)
     