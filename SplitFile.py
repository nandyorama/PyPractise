inputFile = "display_info.log"

import os
import time 
import math
import logging
from os import path
logging.basicConfig(filename='example.log', level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

def read(fileName):
	#return [x for i, x in enumerate(fileName) if i > lineRange]
	f = open(fileName)
	lines = f.readlines()
	return lines

#TODO LIST: GetCWD and create a new Directory to Store New Files	
def getFolder(folderName):
	if not os.path.exists(folderName):
		os.makedirs(folderName)
		os.chdir(folderName)
		return os.getcwd()
	
def splitUtil(file,numSplit,lineRange,fileContent):
	fileName,ext= os.path.splitext(file)
	ii,jj = 0,0
	folder = getFolder("Split")+"/"
	for n in range(numSplit):
		newFile = folder+fileName+"_"+str(n)+ext
		ii = jj
		jj = ii + lineRange
		#print("New File Name is {} and Line Range is {}-{}".format(newFile,ii,jj))
		logging.info("New File Name is {} and Line Range is {}-{}".format(newFile,ii,jj))
		if not(path.isfile(newFile)):
			file = open(newFile,'w')
			#file.write(str(fileContent[ii:jj]))
			#Iterarte to write into file
			for line in fileContent[ii:jj]:
				file.write(line)
			file.close()

""""			
def countLineInFile(fileName):
	count = 0
	for line in open(fileName):
		count += 1
	return count
"""
	
def splitFile(file,numSplit):
	fileContent = read(file)
	count = len(fileContent)
	#print("Number of lines present in file {} is {}".format(file,count))
	logging.info("Number of lines present in file {} is {}".format(file,count))
	#count = countLineInFile(file)
	if count < numSplit:
		print("Not Enough Line to Split")
		return
	lineRange = int(count/numSplit)
	#print("Each file will have {} number of Lines.".format(lineRange))
	logging.info("Each file will have {} number of Lines.".format(lineRange))
	splitUtil(file,numSplit,lineRange,fileContent)
	
t1 = time.time()
num = input("Enter the number of split needed...")
splitFile(inputFile,int(num))		
t2 = time.time()
#print("Time taken to execute CountLine function is "+str(t2-t1))
logging.info("Time taken to execute CountLine function is {}".format(str(t2-t1)))
