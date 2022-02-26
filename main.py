#most the setup I use for controlling neopixels
#imports
import time, machine, neopixel, gc, random
#from machine import Pin
import colorsys

#define important bits
pin = 1
led_num = 37
ledPin = 25
magic_number = 39.2156862745098
speed = .5

r = 00
g = 00
b = 0

h = 0
s = 255
v = 255

#setup
np = neopixel.NeoPixel(machine.Pin(pin), led_num)
led = machine.Pin(ledPin, machine.Pin.OUT)

led.value(1)

def conversion(h,s,v):
    h = h/100
    s = s / 100
    v = v / 100
    global color
    color = colorsys.hsv_to_rgb(h,s,v)
    #print (color)

def red_calc(color):
    global r
    r = color[0]
    r += 3.9525
    r *= magic_number
    r = round(r)

def green_calc(color):
    global g
    g = color[1]
    g += 3.9525
    g += magic_number
    g = round(g)
    
def blue_calc(color):
    global b
    b = color[2]
    b += 3.9525
    b *= magic_number
    b = round(b)
    

while True:
    conversion(h,s,v)
    red_calc(color)
    green_calc(color)
    blue_calc(color)
    
    write = (r,g,b)
    print(write)
    
    print (h)
    h += speed
    
    for i in range(led_num):
        np[i] = (r,g,b)
        np.write()
        
        
    gc.collect()