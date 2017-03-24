#!/usr/bin/env python3
import socket
import datetime
import time
import RPi.GPIO as GPIO


from instapush import Instapush, App
app = App(appid='*****', secret='*****')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

PinLDR = 27
T_NONE=11000
T_LIGHT=4000

def ReadLDR():
    LDRCount = 0 # Sets the count to 0
    GPIO.setup(PinLDR, GPIO.OUT)
    GPIO.output(PinLDR, GPIO.LOW)
    time.sleep(0.1) # Drains all charge from the capacitor
    GPIO.setup(PinLDR, GPIO.IN) # Sets the pin to be input
    # While the input pin reads ‘off’ or Low, count
    while (GPIO.input(PinLDR) == GPIO.LOW):
        LDRCount += 1 # Add one to the counter
    return LDRCount

def check_light():
    out = ReadLDR()
    print(out)
    if out <= T_LIGHT:
        return True
    elif out >= T_NONE:
        return False
    else:
        return True

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def wait_till_next():
    while time_in_range(START_NIGHT, END_NIGHT, datetime.datetime.now().time()):
        time.sleep(30)

def send():
    app.notify(event_name='alert', trackers={ 'id': socket.gethostname()})

START_NIGHT=datetime.time(23, 0, 0)
END_NIGHT=datetime.time(2, 30, 0)

once = False
already = False

while True:
    if time_in_range(START_NIGHT, END_NIGHT, datetime.datetime.now().time()):
        if not check_light():
            if once==True and already==False:
                send()
                once=False
                already=True
                wait_till_next()
                already=False
            elif once==False and already==False:
                once=True
        else:
            once=False
    time.sleep(30)
