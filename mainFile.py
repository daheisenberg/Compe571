import os, os.path
import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)


GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(13,GPIO.IN)

#FOR PWM
GPIO.setup(40,GPIO.OUT)
p = GPIO.PWM(40,50)
p.start(7.5)

def moveCenter():
	#center
	p.ChangeDutyCycle(7.5)
	time.sleep(1)

def moveLeft():
	#left
	p.ChangeDutyCycle(12.5)
	time.sleep(1)
	
def moveRight():
	#right
	p.ChangeDutyCycle(2.5)
	time.sleep(1)

buttonStatus = 0	#not pressed, if pressed it will reset to initial and "ignore the sensors"


while True:

	i= GPIO.input(11)
	j= GPIO.input(12)
	buttonStatus =GPIO.input(13)
	

#there is some noise on the sensor, it is going to record with a filter only.
	if i == 0 and buttonStatus == 0:
		print "no intruders On left" , i
		GPIO.output(3,0)
		time.sleep(1)
	
	if i == 1 and buttonStatus == 0:
		print "intruder On left" , i
		GPIO.output(3,1)
		#os.system("python captureImage.py") 
		moveLeft()
		time.sleep(1)
		continue 		#this will analyze again the input
		
	if j == 0 and buttonStatus == 0:
		print "no intruders On right" , j
		GPIO.output(5,0)
		time.sleep(1)
		continue
		
	if j == 1 and buttonStatus == 0:
		print "intruders On right" , j
		GPIO.output(5,1)
		moveRight()
		#os.system("python captureImage.py")
		time.sleep(1)	
		continue
		
	if buttonStatus == 1:
		print "buttonPressed"
		moveCenter()
		time.sleep(3)
			
		
				
		
		
		








