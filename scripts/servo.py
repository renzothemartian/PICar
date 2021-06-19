# __________________ SOURCE
# https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/


# __________________ PINS
# Black – comes to GND(pin 6) from the Pi
# Red – comes to 3V3(pin 1) from the Pi
# Yellow/Orange – to a free GPIO pin(e.g., GPIO17, pin 11)


# https: // pypi.org/project/RPi.GPIO/
import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
freq = 120
_ogfreq = 120
_maxfreq = 300

p = GPIO.PWM(servoPIN, 120)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization
print("start")
try:
  while True:
    print('Run')

    # p.ChangeDutyCycle(5)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(7.5)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(10)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(12.5)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(10)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(7.5)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(5)
    # time.sleep(0.5)
    # p.ChangeDutyCycle(2.5)
    # time.sleep(0.5)
    p.start(1)

    if freq < _maxfreq
      freq += 50
    else:
      freq = _ogfreq
      
    p.ChangeFrequency(freq)   # where freq is the new frequency in Hz    # input('Press return to stop:')   # use raw_input for Python 2
    # p.stop()
    # GPIO.cleanup()
except KeyboardInterrupt:
  print("stop")
  p.stop()
  GPIO.cleanup()
