import RPi.GPIO as GPIO

import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)

p = GPIO.PWM(40,50)
p.start(7.5)


try:
		while True:
			#center
			p.ChangeDutyCycle(7.5)
			time.sleep(1)
			#left
			p.ChangeDutyCycle(12.5)
			time.sleep(1)
			#right
			p.ChangeDutyCycle(2.5)
			 time.sleep(1)
			
except KeyboardInterrupt:
	GPIO.cleanup()





#pwm = GPIO.PWM(40,50)


#for x in range (0,1):
#	pwm.start(1)
#	print x
#	time.sleep(.5)
	




