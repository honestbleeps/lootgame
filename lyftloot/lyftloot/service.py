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

class LightService:
    on = {'on': True, 'bri': 254, 'transitiontime': 0}
    off = {'on': False, 'bri': 0, 'transitiontime': 0}
    on_no_bri = {'on': True, 'bri': 0, 'transitiontime': 0}
    # off = {'on': False, 'transitiontime': 0}

    pink = {'transitiontime' : 0, 'bri': 254, 'xy': [0.4149, 0.1776]}
    white =  {'transitiontime' : 0, 'bri': 254, 'xy': [0.3227,0.329]}
    red = {'transitiontime': 1, 'bri': 254, 'xy': [0.7, 0.2986]}
    red_dark = {'transitiontime': 1, 'bri': 20, 'xy': [0.7, 0.2986]}
    green = {'transitiontime': 10, 'bri': 254, 'xy': [0.214, 0.709]}

    def __init__(self):
        self.bridge = Bridge('10.59.6.13')
        # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
        self.bridge.connect()
        # Get the bridge state (This returns the full dictionary that you can explore)
        #print b.get_api()

    @postpone
    def game_start(self):
        c = 0
        self.bridge.set_light(3, self.on)
        while c < 10:
            self.bridge.set_light(3, self.pink)
            time.sleep(.2)
            self.bridge.set_light(3, self.white)
            time.sleep(.2)
            c += 1
        self.bridge.set_light(3, self.off)


    @postpone
    def correct(self):
        self.bridge.set_light(3, self.on_no_bri)
        self.bridge.set_light(3, self.green)
        time.sleep(2)
        self.bridge.set_light(3, self.off)

    @postpone
    def incorrect(self):
        c = 0
        while c < 5:
            self.bridge.set_light(3, self.red)
            self.bridge.set_light(3, self.on)
            time.sleep(.1)
            self.bridge.set_light(3, self.red_dark)
            time.sleep(.1)
            c += 1
        self.bridge.set_light(3, self.off)


