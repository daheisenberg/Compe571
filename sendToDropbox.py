import dropbox

import os


import sys


DIR = '/home/pi/Desktop/Project571/sendToDropbox'
numberOfFiles = str (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
print numberOfFiles

sendFile = str('/intruder'+numberOfFiles+'.avi')

fileToOpen = 'sendToDropbox/video2Go' + numberOfFiles + '.avi'

f = open(fileToOpen, 'rb') 

dbx = dropbox.Dropbox ('gFTH8yYgQ8AAAAAAAAAACoJs3XHwDnOJCtqe9UxA3TxOd9Ed0iKGCJceG3a3kTtV')

dbx.files_upload(f.read(), sendFile, mute = True)

f.close()

print "upload to Dropbox Completed"



