import os, os.path
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)


GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.IN)


while True:

	i= GPIO.input(11)
	j= GPIO.input(12)

#hello
	if i == 0:
		print "no intruders On left" , i
		GPIO.output(3,0)
		time.sleep(.3)
	
	if i == 1:
		print "intruder On left" , i
		GPIO.output(3,1)
		#os.system("python captureImage.py") 
		time.sleep(.3)
		
	if j == 0:
		print "no intruders On right" , j
		GPIO.output(5,0)
		time.sleep(.3)
		
	if j == 1:
		print "intruders On right" , j
		GPIO.output(5,1)
		#os.system("python captureImage.py")
		time.sleep(.3)		








