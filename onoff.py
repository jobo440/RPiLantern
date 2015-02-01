import RPi.GPIO as GPIO
from time import sleep
import thread

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def fast():
    while True:
        GPIO.output(11, True)
        sleep(.08)
        GPIO.output(11, False)
        sleep(.08)

def med():
    while True:
        GPIO.output(13, True)
        sleep(.2)
        GPIO.output(13, False)
        sleep(.2)

def slow():
    while True:
        GPIO.output(15, True)
        sleep(2)
        GPIO.output(15, False)
        sleep(2)

thread.start_new_thread(slow,())
thread.start_new_thread(fast,())
thread.start_new_thread(med,())

raw_input("press enter to exit")
