import os

path = "."
def search(path):
	for dirName in os.walk(path):
		print(dirName)
		
def searchOnlyDirectoryRecursively(path):
	for dirName,sub,fileList in os.walk(path):
		print(dirName)

			
def searchOnlyFileRecursively(path):
	for dirName,sub,fileList in os.walk(path):
		for file in fileList:
			print(file)

def searchFileRWithPathRecursively(path):
	for dirName,sub,fileList in os.walk(path):
		#print("Below File Present in Directory {}".format(dirName))
		
		for file in fileList:
			print(dirName+"\\"+file)
			
searchFileRWithPathRecursively(path)
search(path)
