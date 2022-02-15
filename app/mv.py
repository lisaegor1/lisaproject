# importing os module
import os
import shutil

def mv():

	path = '/app'
	source = 'sg.txt'
	destination = 'templates'
	sourcePath = path+'/'+source
	destinationPath = path+'/'+destination
	if os.path.isdir(destinationPath+'/'+source):
		print(source, 'exists in the destination path!')
		shutil.rmtree(destinationPath+'/'+source)
	
	elif os.path.isfile(destinationPath+'/'+source):
		os.remove(destinationPath+'/'+source)
		print(source, 'deleted in', destination)


	dest = shutil.move(sourcePath, destinationPath)



