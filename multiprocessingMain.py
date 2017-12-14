from multiprocessing import Process
from threading import Thread
import threading
import os, os.path
import RPi.GPIO as GPIO
import time
import sys
import subprocess


#All GPIO SETTINGS
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


#create a lock
myLock = threading.Lock()

def loop_left_sensor():
	#testing for left side
	lockMotor = 0
	filterForLeft = 0
	
	while 1:
		i = 0
		i= GPIO.input(12)		#left
	
		
		
	#there is some noise on the sensor, it is going to record with a filter only.
		if i == 1 and filterForLeft < 3:		
			#print str(i) + "what"
			filterForLeft = filterForLeft + 1
			print "maybe i detected something on the left"
			print filterForLeft
			print("a")
			time.sleep(1)
	
		if i == 0 :
			print "resting on the left"
			#reset filters
			filterForLeft = 0
			filterForRight = 0
			if(lockMotor == 0):
				moveCenter()	#move it once			
			time.sleep(.3)
	 
	 #Critical section going to start
		if filterForLeft > 2:
			print ("intruder On left" , i)
			GPIO.output(3,1)
			#Get into critical sectionlock and secure LOCK
			myLock.acquire(True)
			moveLeft()
			os.system("python captureImage.py") 		#this command has to wait to be finished
			os.system('clear')							#this can be thrown as background process
			avantiDropbox()
			#end critical section
			myLock.release() 							#release the lock
			filterForLeft = 0
			GPIO.output(3,0)
			time.sleep(2)
	 
			
	#thread for right sensor for right side
def loop_right_sensor():
	filterForRight = 0

	while 1:
		j = 0
		j= GPIO.input(37)		#right


		if j == 1 and filterForRight < 3:
			filterForRight = filterForRight + 1
			print "maybe i detected something on the right"
			print filterForRight
			time.sleep(1)

		if i == 0 :
			print "resting on the left"
			#reset filter
			filterForRight = 0
			if(lockMotor == 0):
				moveCenter()	#move it once			
			time.sleep(.3)
		
		#for locks i used the following tutorial
		#blog.acipo.com/python-thread-locking/
		if filterForRight > 2 :
			print "intruders On right" , j
			GPIO.output(5,1)
			#get the lock to go to critical section
			myLock.acquire(True)
			moveRight()
			os.system("python ../captureImage.py")
			os.system('clear')							#this can be thrown as background process
			avantiDropbox()
			myLock.release()
			filterForRight = 0
			GPIO.output(5,0)					
			time.sleep(2)	


#start threads 	
threadA = Thread(target = loop_left_sensor())
threadB = Thread(target = loop_right_sensor())	
	
threadA.run()
threadB.run()

threadA.join()
threadB.join()	
	
