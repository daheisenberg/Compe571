import dropbox

import sys

f = open('sendToDropbox/video2Go2.avi', 'rb') 

dbx = dropbox.Dropbox ('gFTH8yYgQ8AAAAAAAAAACoJs3XHwDnOJCtqe9UxA3TxOd9Ed0iKGCJceG3a3kTtV')

dbx.files_upload(f.read(), '/intruder.avi', mute = True)

f.close()

print "upload to Dropbox Completed"



