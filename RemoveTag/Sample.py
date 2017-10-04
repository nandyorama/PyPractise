import re
import os,sys
path = "."
pattern = '<french>(.*?)</french>'

def find_all_matches(fileContent):
	matches = re.findall(pattern , fileContent, re.DOTALL)
	return (matches)

def mainFun(inputFile):	
	inputFileContent = open(inputFile, "r").read()
	result = find_all_matches(inputFileContent)
	for i in result:
		inputFileContent = inputFileContent.replace(i, "")
		#print inputFileContent
		#print "*************"
	
	handle = open(inputFile, 'w')
	handle.write(inputFileContent)
	handle.close()

def start():
	dirs = os.listdir( path )	
	for file in dirs:
		#print file
		filename, file_extension = os.path.splitext(file)
		if file_extension==".xml":
			#print "*********"
			mainFun(file)
			
start()
