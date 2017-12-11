import time
from subprocess import call
import os, os.path
import shutil
import RPi.GPIO as GPIO

from datetime import datetime


#The amperage of the webcam is not enough, it restarts, works 1-10 times.
#delete previous avi
#bad idea erases everything!
#call(["find", "." ,"-name" ,"*.avi" ,"-type" ,"f", "-delete"])

#get the number of files to archive all videos

DIR = '/home/pi/Desktop/Project571/sendToDropbox'
numberOfFiles = str (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
print numberOfFiles
tokenInt = int(numberOfFiles) + 1

print tokenInt
numberOfFiles = str(tokenInt)				

print numberOfFiles

newFileName = "video2Go" + numberOfFiles + ".avi"

for i in xrange(1,10):
	#for image only
	#call(["fswebcam", "-d", "/dev/video0", "-r", "1280x720", "--no-banner", "thefile.jpg"])
	
	call(["avconv", "-t", "5",  "-f",  "video4linux2" , "-i", "/dev/video0", newFileName])
	os.system('clear')							#this can be thrown as background process	
	time.sleep(1)


print newFileName

source = '/home/pi/Desktop/Project571/' + newFileName
destination = '/home/pi/Desktop/Project571/sendToDropbox/' + newFileName

shutil.copy2(source, destination) # complete target filename given

os.remove(source)

print "Finished Capturing Image"

