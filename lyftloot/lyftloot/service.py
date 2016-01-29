from threading import Thread
from phue import Bridge
import time
#import logging

#logging.basicConfig()

def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


b = Bridge('10.59.6.13')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
#print b.get_api()

on = {'on': True, 'bri': 254, 'transitiontime': 0}
off = {'on': False, 'bri': 0, 'transitiontime': 0}
on_no_bri = {'on': True, 'bri': 0, 'transitiontime': 0}
# off = {'on': False, 'transitiontime': 0}

pink = {'transitiontime' : 0, 'bri': 254, 'xy': [0.4149, 0.1776]}
white =  {'transitiontime' : 0, 'bri': 254, 'xy': [0.3227,0.329]}
red = {'transitiontime': 1, 'bri': 254, 'xy': [0.7, 0.2986]}
red_dark = {'transitiontime': 1, 'bri': 20, 'xy': [0.7, 0.2986]}
green = {'transitiontime': 10, 'bri': 254, 'xy': [0.214, 0.709]}

@postpone
def game_start():
    c = 0
    b.set_light(3, on)
    while c < 10:
        b.set_light(3, pink)
        time.sleep(.2)
        b.set_light(3, white)
        time.sleep(.2)
        c += 1
    b.set_light(3, off)


@postpone
def correct():
    b.set_light(3, on_no_bri)
    b.set_light(3, green)
    time.sleep(2)
    b.set_light(3, off)

@postpone
def incorrect():
    c = 0
    while c < 5:
        b.set_light(3, red)
        b.set_light(3, on)
        time.sleep(.1)
        b.set_light(3, red_dark)
        time.sleep(.1)
        c += 1
    b.set_light(3, off)

# game_start()
# correct()
# incorrect()



