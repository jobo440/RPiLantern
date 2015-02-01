import RPi.GPIO as GPIO
import time
import thread

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11,50)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

p.start(0)


	while True:
		for i in range(100):
			p.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range(100):
			p.ChangeDutyCycle(100-i)
			time.sleep(0.02)



p.stop()






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
