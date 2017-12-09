

#open file to read number of files uploaded
fo = open('../sendToDropbox/filesUploaded.txt','r')
numberOfFiles =  str(fo.read())

numberOfFilesInt = int(numberOfFiles)

fo.close()
 
numberOfFilesInt = numberOfFilesInt + 1

#print numberOfFiles
f = open('../sendToDropbox/filesUploaded.txt','w')
f.write(str(numberOfFilesInt))
f.close()


