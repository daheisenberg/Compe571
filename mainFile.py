import os, os.path
import RPi.GPIO as GPIO
import time
import sys
import subprocess


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)


GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(37,GPIO.IN)

#FOR PWM
GPIO.setup(40,GPIO.OUT)
p = GPIO.PWM(40,50)
p.start(7.5)

def avantiDropbox():
	print "Avanti with dropbox"
	p = subprocess.Popen([sys.executable, '/home/pi/Desktop/Project571/sendToDropbox.py'],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

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

buttonStatus = False	#not pressed, if pressed it will reset to initial and "ignore the sensors"

filterForLeft = 0
filterForRight = 0

#To avoid moving it
lockMotor = 0


#clear the input
os.system  ('clear')


while True:

	i = 0
	j = 0
	i= GPIO.input(37)		#left
	j= GPIO.input(12)		#right
	buttonPressed =GPIO.input(13)
	
#there is some noise on the sensor, it is going to record with a filter only.

	if i == 1 and filterForLeft < 3:		
		#print str(i) + "what"
		filterForLeft = filterForLeft + 1
		print "maybe i detected something on the left"
		print filterForLeft
		time.sleep(1)
		continue
			
	if j == 1 and filterForRight < 3:
		filterForRight = filterForRight + 1
		print "maybe i detected something on the right"
		print filterForRight
		time.sleep(1)
		continue

#ending filter

	if i == 0 and j == 0:
		print "resting"
		#reset filters
		filterForLeft = 0
		filterForRight = 0
		if(lockMotor == 0):
			moveCenter()	#move it once	
			lockMotor = 1
		time.sleep(.3)
		continue 

#end filter

	if i == 0 and buttonStatus == False:
		print "no intruders On left" , i
		GPIO.output(3,0)
		time.sleep(1)
	
	if filterForLeft > 2 :
		print "intruder On left" , i
		GPIO.output(3,1)
		moveLeft()
		os.system("python captureImage.py") 		#this command has to wait to be finished
		os.system('clear')							#this can be thrown as background process
		avantiDropbox()
		filterForLeft = 0
		GPIO.output(3,0)
		
		lockMotor = 0
		
		time.sleep(2)
		continue 		#this will analyze again the input
		
	if j == 0 and buttonStatus == False:
		print "no intruders On right" , j
		GPIO.output(5,0)
		time.sleep(1)
		continue
		
	if filterForRight > 2 :
		print "intruders On right" , j
		GPIO.output(5,1)
		moveRight()
		os.system("python captureImage.py")
		os.system('clear')							#this can be thrown as background process
		avantiDropbox()
		filterForRight = 0
		GPIO.output(5,0)
		
		lockMotor = 0 
		
		time.sleep(2)	
		continue
	
	#this button was intended to reset without waiting for it. 	
	if buttonPressed == 1:
		print "buttonPressed"
		buttonStatus = not buttonStatus
		moveCenter()
		time.sleep(3)
			
		
				
		
		
		








