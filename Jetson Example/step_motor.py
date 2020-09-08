import sys
print(sys.version)

import Jetson.GPIO as GPIO
import time

# Parameter
pulse_per_rev = 200 # choice in 200, 400, 800, 1600, 3200, 6400 (unit : pulse/rev)
pulse_delay = 0.001		# unit : sec
delay_time = 1	# unit : sec

# for linear actuator
lead = 2	# unit : mm

# Pin Definitons:
PUL = 29  # BOARD pin 29
DIR = 33  # BOARD pin 33

print('\n Resolution : ', lead/pulse_per_rev, 'mm/pulse \n')

# Function of Step motor
def give_pulse( PUL, pulse_per_rev, pulse_delay, delay_time):
	
	for i in range(0,pulse_per_rev):
		GPIO.output(PUL, GPIO.HIGH)
		time.sleep(pulse_delay)
		GPIO.output(PUL, GPIO.LOW)
		time.sleep(pulse_delay)

	time.sleep(delay_time)


# Pin Setup:
GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
GPIO.setup(PUL, GPIO.OUT)  # Pulse pin set as output
GPIO.setup(DIR, GPIO.OUT)  # Direction pin set as output

# Run Step Motor 
GPIO.output(DIR, GPIO.LOW)
give_pulse( PUL, pulse_per_rev, pulse_delay, delay_time)

GPIO.output(DIR, GPIO.HIGH)
give_pulse( PUL, pulse_per_rev, pulse_delay, delay_time)

# Cleanup GPIO
GPIO.cleanup()


