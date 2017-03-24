import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

PinLDR = 27
T_NONE=1100
T_LIGHT=750

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
    return out

print("cover the light")
time.sleep(5)
print("T_NONE=")
check_light()
print("Uncover the light")
time.sleep(5)
print("T_LIGHT=")
check_light()
